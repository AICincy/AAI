import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent / "krass_skill_suite_tests.py"
MODULE_NAME = "krass_skill_suite_tests"
ROUTER_TEST_DESCRIPTION = (
    "test metadata for mode selection with Continue flow, "
    "verification-focused drafting, risk, and provenance"
)


def load_suite_module():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if not spec or not spec.loader:
        raise ImportError(f"Unable to load module spec for {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class KrassSkillSuiteHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = load_suite_module()

    def test_frontmatter_parses_valid_block(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "SKILL.md"
            path.write_text("---\nname: sample\ndescription: sample description\n---\nBody text\n", encoding="utf-8")

            meta, body = self.suite.frontmatter(path)

            self.assertEqual(meta["name"], "sample")
            self.assertEqual(meta["description"], "sample description")
            self.assertEqual(body, "Body text\n")

    def test_frontmatter_rejects_malformed_line(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "SKILL.md"
            path.write_text("---\nname: sample\nmalformed\n---\nBody\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                self.suite.frontmatter(path)

    def test_has_terms_is_case_insensitive(self):
        text = "Risk Tier and SOURCE LEDGER are required."
        missing = self.suite.has_terms(text, ["risk tier", "source ledger", "mode confidence"])
        self.assertEqual(missing, ["mode confidence"])

    def test_mk_result_pass_warn_fail_and_priority(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            passed = self.suite.mk_result(
                "run1",
                "abc123",
                "krass-core-contracts",
                "id.pass",
                "behavioral_routing",
                [self.suite.Subcheck(True, "a", "ok"), self.suite.Subcheck(True, "b", "ok")],
                root,
            )
            self.assertEqual(passed.result, "pass")
            self.assertEqual(passed.points_earned, self.suite.WEIGHTS["behavioral_routing"])

            warned = self.suite.mk_result(
                "run1",
                "abc123",
                "krass-core-contracts",
                "id.warn",
                "behavioral_routing",
                [self.suite.Subcheck(True, "a", "ok"), self.suite.Subcheck(False, "b", "bad", "f", "r", "P2")],
                root,
            )
            self.assertEqual(warned.result, "warn")
            self.assertEqual(warned.priority, "P2")

            failed = self.suite.mk_result(
                "run1",
                "abc123",
                "krass-core-contracts",
                "id.fail",
                "behavioral_routing",
                [
                    self.suite.Subcheck(False, "a", "bad", "f1", "r1", "P2"),
                    self.suite.Subcheck(False, "b", "bad", "f2", "r2", "P0"),
                ],
                root,
            )
            self.assertEqual(failed.result, "fail")
            self.assertEqual(failed.points_earned, 0)
            self.assertEqual(failed.priority, "P0")
            self.assertIn(MODULE_PATH.name, failed.retest_command)

    def test_summarize_computes_skill_and_suite_percentages(self):
        rows = [
            self.suite.TestResult("r", "c", "s1", "t1", "d", "pass", 10, 10, "", "", "", "P3", ""),
            self.suite.TestResult("r", "c", "s1", "t2", "d", "warn", 5, 10, "", "", "", "P2", ""),
            self.suite.TestResult("r", "c", "s2", "t3", "d", "pass", 20, 20, "", "", "", "P3", ""),
        ]

        by_skill, suite_score = self.suite.summarize(rows)

        self.assertEqual(by_skill["s1"], 75.0)
        self.assertEqual(by_skill["s2"], 100.0)
        self.assertEqual(suite_score, 87.5)

    def test_write_reports_writes_json_csv_and_markdown(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rows = [
                self.suite.TestResult("rid", "sha", "skill-a", "id1", "structural_validity", "pass", 20, 20, "ok", "", "", "P3", "py cmd"),
                self.suite.TestResult("rid", "sha", "skill-a", "id2", "behavioral_routing", "warn", 10, 20, "warn", "reason", "fix", "P1", "py cmd"),
            ]

            paths = self.suite.write_reports(root, "rid", "sha", rows)

            payload = json.loads(paths["json"].read_text(encoding="utf-8"))
            self.assertEqual(payload["run_id"], "rid")
            self.assertEqual(payload["commit"], "sha")
            self.assertEqual(payload["suite_success_percent"], 75.0)
            self.assertEqual(len(payload["remediation_queue"]), 1)

            with paths["csv"].open(encoding="utf-8") as fh:
                csv_rows = list(csv.DictReader(fh))
            self.assertEqual(len(csv_rows), 2)
            self.assertEqual(csv_rows[1]["result"], "warn")

            md = paths["markdown"].read_text(encoding="utf-8")
            self.assertIn("# Krass Skill Suite Test Report", md)
            self.assertIn("Remediation Queue", md)

    def test_structural_checks_report_missing_validator(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = "krass-cognitive-router"
            skill_dir = root / skill
            (skill_dir / "agents").mkdir(parents=True)
            (skill_dir / "references").mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                f"---\nname: krass-cognitive-router\ndescription: {ROUTER_TEST_DESCRIPTION}\n---\n",
                encoding="utf-8",
            )
            (skill_dir / "agents" / "openai.yaml").write_text("name: x\n", encoding="utf-8")
            for ref in self.suite.EXPECTED_REFERENCES[skill]:
                (skill_dir / "references" / ref).write_text("content\n", encoding="utf-8")

            checks = self.suite.structural_checks(root, skill)

            self.assertTrue(checks[0].ok)
            self.assertTrue(checks[1].ok)
            self.assertTrue(checks[2].ok)
            self.assertTrue(checks[3].ok)
            self.assertEqual(checks[4].label, "quick_validate.py")
            self.assertFalse(checks[4].ok)

    def test_metadata_checks_fail_for_invalid_name(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = "krass-cognitive-router"
            skill_md = root / skill / "SKILL.md"
            skill_md.parent.mkdir(parents=True)
            skill_md.write_text(
                f"---\nname: wrong-name\ndescription: {ROUTER_TEST_DESCRIPTION}\n---\nBody\n",
                encoding="utf-8",
            )

            checks = self.suite.metadata_checks(root, skill)

            by_label = {c.label: c for c in checks}
            self.assertFalse(by_label["name matches folder"].ok)
            self.assertTrue(by_label["frontmatter keys"].ok)

    def test_logging_checks_detect_missing_gitignore_entry(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / ".gitignore").write_text("*.tmp\n", encoding="utf-8")

            checks = self.suite.logging_checks(root, "krass-core-contracts", "run-1")

            self.assertFalse(checks[0].ok)
            self.assertTrue(checks[1].ok)
            self.assertTrue(checks[2].ok)


if __name__ == "__main__":
    unittest.main()
