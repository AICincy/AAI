#!/usr/bin/env python3
"""Deterministic test harness for the Krass Codex skill suite."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


SKILLS = [
    "krass-core-contracts",
    "krass-cognitive-router",
    "krass-communication-calibrator",
    "krass-constraint-verifier",
    "krass-context-loader",
    "krass-artifact-builder",
    "krass-quality-auditor",
]

WEIGHTS = {
    "structural_validity": 20,
    "trigger_metadata": 15,
    "reference_integrity": 15,
    "cognitive_contract_compliance": 20,
    "behavioral_routing": 20,
    "logging_and_auditability": 10,
}

LOG_FIELDS = [
    "run_id",
    "commit",
    "skill",
    "test_id",
    "dimension",
    "result",
    "points_earned",
    "points_possible",
    "evidence",
    "failure_reason",
    "remediation",
    "priority",
    "retest_command",
]

EXPECTED_REFERENCES = {
    "krass-core-contracts": [
        "cognitive_interface_contract.md",
        "handoff_contract.md",
        "mode_routing.md",
        "confidence_summary.md",
        "register_matrix.md",
    ],
    "krass-cognitive-router": ["routing_workflow.md"],
    "krass-communication-calibrator": [
        "recipient_posture.md",
        "drafting_constraints.md",
    ],
    "krass-constraint-verifier": ["verification_matrix.md", "local_constraints.md"],
    "krass-context-loader": ["context_taxonomy.md"],
    "krass-artifact-builder": ["artifact_routing.md", "output_policy.md"],
    "krass-quality-auditor": ["audit_matrix.md", "failure_modes.md"],
}

DESCRIPTION_TERMS = {
    "krass-core-contracts": ["AuDHD", "handoff", "mode routing", "confidence"],
    "krass-cognitive-router": ["mode", "Continue", "drafting", "verification"],
    "krass-communication-calibrator": ["Drafts", "ADA", "regulator", "tone"],
    "krass-constraint-verifier": ["CareSource", "public transit", "citations", "current"],
    "krass-context-loader": ["prior work", "medical", "legal", "transit"],
    "krass-artifact-builder": ["DOCX", "XLSX", "PPTX", "React", "PDF"],
    "krass-quality-auditor": ["cognitive-interface", "factual", "reversibility", "confidence"],
}

REFERENCE_PHRASES = {
    "krass-core-contracts": {
        "references/cognitive_interface_contract.md": [
            "not framed as a deficit",
            "pattern compression",
            "monotropic focus",
            "asymmetric working memory",
            "senior-level",
        ],
        "references/handoff_contract.md": [
            "Skills do not perform autonomous background messaging",
            "Task Packet",
            "verification_required",
            "confidence_summary",
        ],
        "references/mode_routing.md": ["Continue", "draft", "review", "chat"],
        "references/confidence_summary.md": ["Sources", "Assumptions", "Uncertainty", "Scope limits"],
        "references/register_matrix.md": [
            "Statutory authority",
            "Adversarial precision",
            "Collegial directness",
        ],
    },
    "krass-cognitive-router": {
        "SKILL.md": [
            "task_packet",
            "krass-context-loader",
            "krass-constraint-verifier",
            "krass-communication-calibrator",
            "krass-artifact-builder",
            "krass-quality-auditor",
        ],
        "references/routing_workflow.md": [
            "primary_objective",
            "dependency order",
            "Continue",
            "verification_required",
            "artifact_required",
        ],
    },
    "krass-communication-calibrator": {
        "SKILL.md": ["recipient class", "desired action", "evidence posture", "hedging"],
        "references/recipient_posture.md": [
            "ADA coordinator",
            "Opposing party",
            "Professional peer",
            "Personal contact",
        ],
        "references/drafting_constraints.md": [
            "One communication",
            "no hedging",
            "deadline",
            "tone",
        ],
    },
    "krass-constraint-verifier": {
        "SKILL.md": ["CareSource Medicaid", "public transit", "primary sources"],
        "references/verification_matrix.md": ["Legal citation", "Transit route", "Source Discipline"],
        "references/local_constraints.md": [
            "Deer Park, Ohio",
            "Metro routes 4, 5, MetroNow, Metro Access",
            "CareSource Medicaid",
        ],
    },
    "krass-context-loader": {
        "SKILL.md": ["context_packet", "medical", "legal", "provider", "financial", "transit"],
        "references/context_taxonomy.md": ["Known", "Inferred", "Stale", "Missing", "Sensitive"],
    },
    "krass-artifact-builder": {
        "SKILL.md": ["absolute paths", "Create the artifact", "validation"],
        "references/artifact_routing.md": [
            "documents:documents",
            "spreadsheets:Spreadsheets",
            "presentations:Presentations",
            "build-web-apps:frontend-app-builder",
            "PDF",
        ],
        "references/output_policy.md": ["absolute paths", "Validate created files"],
    },
    "krass-quality-auditor": {
        "SKILL.md": ["deficit framing", "pedagogical scaffolding", "confidence summary"],
        "references/audit_matrix.md": ["Cognitive framing", "Verification", "Reversibility"],
        "references/failure_modes.md": [
            "Source fabrication",
            "Local impracticality",
            "Artifact theater",
            "Recap burden",
        ],
    },
}

BEHAVIOR_CHECKS = {
    "krass-core-contracts": [
        ("shared cognitive contract", "references/cognitive_interface_contract.md", ["AuDHD", "not framed as a deficit"]),
        ("shared handoff contract", "references/handoff_contract.md", ["mode", "primary_objective", "handoff_notes"]),
        ("shared confidence contract", "references/confidence_summary.md", ["Sources", "Assumptions", "Scope limits"]),
    ],
    "krass-cognitive-router": [
        ("ada draft route", "SKILL.md", ["krass-context-loader", "krass-communication-calibrator", "krass-quality-auditor"]),
        ("provider route", "SKILL.md", ["krass-context-loader", "krass-constraint-verifier", "krass-quality-auditor"]),
        ("continue route", "SKILL.md", ["Continue", "without recap"]),
    ],
    "krass-communication-calibrator": [
        ("ada register", "references/recipient_posture.md", ["ADA coordinator", "Rights-preserving precision"]),
        ("opposing party register", "references/recipient_posture.md", ["Opposing party", "Adversarial precision"]),
        ("tone correction", "references/drafting_constraints.md", ["Revise immediately", "Do not apologize"]),
    ],
    "krass-constraint-verifier": [
        ("caresource gate", "references/local_constraints.md", ["CareSource Medicaid", "provider recommendation"]),
        ("transit gate", "references/local_constraints.md", ["Metro routes 4, 5", "private vehicle"]),
        ("primary source gate", "references/verification_matrix.md", ["official", "Do not include unverifiable claims"]),
    ],
    "krass-context-loader": [
        ("case facts", "references/context_taxonomy.md", ["Medical", "Legal", "Financial"]),
        ("state labels", "references/context_taxonomy.md", ["Known", "Inferred", "Stale", "Missing", "Sensitive"]),
        ("privacy minimization", "SKILL.md", ["Do not expose sensitive context"]),
    ],
    "krass-artifact-builder": [
        ("spreadsheet route", "references/artifact_routing.md", ["XLSX", "spreadsheets:Spreadsheets"]),
        ("document route", "references/artifact_routing.md", ["DOCX", "documents:documents"]),
        ("artifact validation", "references/output_policy.md", ["Validate created files", "absolute paths"]),
    ],
    "krass-quality-auditor": [
        ("defect detection", "references/failure_modes.md", ["Deficit framing", "Source fabrication"]),
        ("audit gates", "references/audit_matrix.md", ["Artifact validity", "Confidence summary"]),
        ("error remediation", "references/failure_modes.md", ["Inaccuracy", "Cause", "Impact", "Remediation"]),
    ],
}

BANNED_PATTERNS = [
    r"TO" + r"DO",
    r"FIX" + r"ME",
    r"PLACE" + r"HOLDER",
    r"AuDHD\s+is\s+a\s+deficit",
    r"autism\s+and\s+ADHD\s+are\s+deficits",
    r"impairment\s+requiring\s+simplification",
    r"explain\s+like\s+I.?m\s+five",
    r"for\s+beginners",
]


@dataclass
class Subcheck:
    ok: bool
    label: str
    evidence: str
    failure_reason: str = ""
    remediation: str = ""
    priority: str = "P3"


@dataclass
class TestResult:
    run_id: str
    commit: str
    skill: str
    test_id: str
    dimension: str
    result: str
    points_earned: float
    points_possible: float
    evidence: str
    failure_reason: str
    remediation: str
    priority: str
    retest_command: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test and score the Krass Codex skill suite.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Skills repository root. Defaults to the parent of tests/.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        choices=SKILLS,
        help="Limit the run to one skill. May be repeated.",
    )
    parser.add_argument(
        "--run-id",
        default=None,
        help="Override the timestamped run id.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter fence")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter fence")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def command_output(args: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout.strip()


def git_commit(root: Path) -> str:
    code, out = command_output(["git", "rev-parse", "--short", "HEAD"], root)
    return out if code == 0 and out else "unknown"


def all_skill_texts(skill_dir: Path) -> list[tuple[Path, str]]:
    files = [skill_dir / "SKILL.md"]
    refs = skill_dir / "references"
    if refs.exists():
        files.extend(sorted(refs.glob("*.md")))
    return [(path, read_text(path)) for path in files if path.exists()]


def has_terms(text: str, terms: Iterable[str]) -> list[str]:
    missing = []
    low = text.lower()
    for term in terms:
        if term.lower() not in low:
            missing.append(term)
    return missing


def mk_result(
    run_id: str,
    commit: str,
    skill: str,
    test_id: str,
    dimension: str,
    subchecks: list[Subcheck],
    root: Path,
) -> TestResult:
    weight = WEIGHTS[dimension]
    passed = sum(1 for c in subchecks if c.ok)
    points = round(weight * (passed / len(subchecks)), 2) if subchecks else 0.0
    if passed == len(subchecks):
        status = "pass"
    elif points > 0:
        status = "warn"
    else:
        status = "fail"
    failures = [c for c in subchecks if not c.ok]
    priority_rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    priority = min((c.priority for c in failures), key=lambda p: priority_rank[p], default="P3")
    evidence = " | ".join(
        f"{'PASS' if c.ok else 'FAIL'} {c.label}: {c.evidence}" for c in subchecks
    )
    failure_reason = " | ".join(c.failure_reason for c in failures)
    remediation = " | ".join(c.remediation for c in failures) or "No remediation required."
    rel_script = Path("tests") / "krass_skill_suite_tests.py"
    retest = f"{sys.executable} {root / rel_script} --skill {skill}"
    return TestResult(
        run_id=run_id,
        commit=commit,
        skill=skill,
        test_id=test_id,
        dimension=dimension,
        result=status,
        points_earned=points,
        points_possible=weight,
        evidence=evidence,
        failure_reason=failure_reason,
        remediation=remediation,
        priority=priority,
        retest_command=retest,
    )


def structural_checks(root: Path, skill: str) -> list[Subcheck]:
    skill_dir = root / skill
    checks = [
        Subcheck(skill_dir.exists(), "skill folder exists", str(skill_dir), "Missing skill folder.", "Restore or recreate the skill folder.", "P0"),
        Subcheck((skill_dir / "SKILL.md").exists(), "SKILL.md exists", str(skill_dir / "SKILL.md"), "Missing SKILL.md.", "Restore SKILL.md with required frontmatter and body.", "P0"),
        Subcheck((skill_dir / "agents" / "openai.yaml").exists(), "agents/openai.yaml exists", str(skill_dir / "agents" / "openai.yaml"), "Missing UI metadata.", "Regenerate agents/openai.yaml with skill-creator tooling.", "P2"),
    ]
    refs = EXPECTED_REFERENCES[skill]
    missing_refs = [ref for ref in refs if not (skill_dir / "references" / ref).exists()]
    checks.append(
        Subcheck(
            not missing_refs,
            "expected references exist",
            ", ".join(refs),
            f"Missing references: {', '.join(missing_refs)}",
            "Restore missing reference files or update the skill contract.",
            "P1",
        )
    )
    validate = root / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
    if validate.exists() and skill_dir.exists():
        code, out = command_output([sys.executable, str(validate), str(skill_dir)], root)
        checks.append(
            Subcheck(
                code == 0,
                "quick_validate.py",
                out or "no output",
                "quick_validate.py failed.",
                "Fix frontmatter, naming, or required skill anatomy; ensure PyYAML is installed for the validator.",
                "P0",
            )
        )
    else:
        checks.append(
            Subcheck(
                False,
                "quick_validate.py",
                str(validate),
                "Validator script is unavailable.",
                "Restore .system/skill-creator or run in a Codex environment containing the validator.",
                "P1",
            )
        )
    return checks


def metadata_checks(root: Path, skill: str) -> list[Subcheck]:
    skill_md = root / skill / "SKILL.md"
    checks: list[Subcheck] = []
    try:
        meta, _ = frontmatter(skill_md)
    except Exception as exc:
        return [
            Subcheck(
                False,
                "frontmatter parses",
                str(exc),
                "Frontmatter could not be parsed.",
                "Repair SKILL.md frontmatter.",
                "P0",
            )
        ]
    keys = set(meta)
    checks.append(
        Subcheck(
            keys == {"name", "description"},
            "frontmatter keys",
            ", ".join(sorted(keys)),
            f"Unexpected frontmatter keys: {sorted(keys)}",
            "Keep only name and description in SKILL.md frontmatter.",
            "P1",
        )
    )
    checks.append(
        Subcheck(
            meta.get("name") == skill,
            "name matches folder",
            meta.get("name", ""),
            "Frontmatter name does not match the folder.",
            "Set frontmatter name to the skill folder name.",
            "P1",
        )
    )
    description = meta.get("description", "")
    missing_terms = has_terms(description, DESCRIPTION_TERMS[skill])
    checks.append(
        Subcheck(
            not missing_terms,
            "description trigger terms",
            description,
            f"Description missing trigger terms: {', '.join(missing_terms)}",
            "Update description with concrete trigger contexts without exposing unnecessary sensitive detail.",
            "P2",
        )
    )
    checks.append(
        Subcheck(
            80 <= len(description) <= 700,
            "description length",
            f"{len(description)} characters",
            "Description is too sparse or too verbose for trigger metadata.",
            "Compress or expand the description to include exact use cases.",
            "P2",
        )
    )
    return checks


def reference_checks(root: Path, skill: str) -> list[Subcheck]:
    skill_dir = root / skill
    checks = []
    for rel, terms in REFERENCE_PHRASES[skill].items():
        path = skill_dir / rel
        if not path.exists():
            checks.append(
                Subcheck(
                    False,
                    f"{rel} exists",
                    str(path),
                    f"Missing required file: {rel}",
                    "Restore the required file or remove stale references.",
                    "P1",
                )
            )
            continue
        text = read_text(path)
        missing = has_terms(text, terms)
        checks.append(
            Subcheck(
                not missing,
                f"{rel} required phrases",
                f"checked {len(terms)} phrases",
                f"{rel} missing: {', '.join(missing)}",
                "Add the missing contract terms or revise the harness expectation if the contract intentionally changed.",
                "P1",
            )
        )
    if skill != "krass-core-contracts":
        skill_text = read_text(skill_dir / "SKILL.md")
        checks.append(
            Subcheck(
                "krass-core-contracts" in skill_text,
                "shared contract linkage",
                "SKILL.md references krass-core-contracts",
                "Skill does not link to the shared core contracts.",
                "Add required references to the shared cognitive and handoff contracts.",
                "P1",
            )
        )
    return checks


def cognitive_checks(root: Path, skill: str) -> list[Subcheck]:
    skill_dir = root / skill
    checks: list[Subcheck] = []
    texts = all_skill_texts(skill_dir)
    combined = "\n".join(text for _, text in texts)
    non_ascii = [(path, re.findall(r"[^\x00-\x7F]", text)) for path, text in texts]
    non_ascii_hits = [f"{path.name}:{''.join(chars[:5])}" for path, chars in non_ascii if chars]
    checks.append(
        Subcheck(
            not non_ascii_hits,
            "ASCII-only content",
            "no non-ASCII characters" if not non_ascii_hits else "; ".join(non_ascii_hits),
            "Non-ASCII punctuation or characters detected.",
            "Replace non-ASCII punctuation with ASCII equivalents unless explicitly required.",
            "P2",
        )
    )
    banned_hits = []
    for pattern in BANNED_PATTERNS:
        if re.search(pattern, combined, flags=re.IGNORECASE):
            banned_hits.append(pattern)
    checks.append(
        Subcheck(
            not banned_hits,
            "banned patterns absent",
            "no banned patterns" if not banned_hits else ", ".join(banned_hits),
            f"Banned content detected: {', '.join(banned_hits)}",
            "Remove template remnants, deficit framing, or pedagogical scaffolding.",
            "P1",
        )
    )
    if skill == "krass-core-contracts":
        contract = read_text(skill_dir / "references" / "cognitive_interface_contract.md")
        required = ["AuDHD", "pattern compression", "monotropic focus", "asymmetric working memory"]
        missing = has_terms(contract, required)
        checks.append(
            Subcheck(
                not missing,
                "cognitive invariant present",
                ", ".join(required),
                f"Cognitive contract missing: {', '.join(missing)}",
                "Restore the cognitive-interface invariant in the shared contract.",
                "P1",
            )
        )
    else:
        skill_text = read_text(skill_dir / "SKILL.md")
        checks.append(
            Subcheck(
                "cognitive_interface_contract.md" in skill_text,
                "uses cognitive contract",
                "SKILL.md references cognitive_interface_contract.md",
                "Skill does not require loading the shared cognitive-interface contract.",
                "Add the cognitive-interface contract to required references.",
                "P1",
            )
        )
    return checks


def behavior_checks(root: Path, skill: str) -> list[Subcheck]:
    skill_dir = root / skill
    checks = []
    for label, rel, terms in BEHAVIOR_CHECKS[skill]:
        path = skill_dir / rel
        if not path.exists():
            checks.append(
                Subcheck(
                    False,
                    label,
                    str(path),
                    f"Behavior source missing: {rel}",
                    "Restore the behavior reference file.",
                    "P1",
                )
            )
            continue
        missing = has_terms(read_text(path), terms)
        checks.append(
            Subcheck(
                not missing,
                label,
                f"checked terms: {', '.join(terms)}",
                f"Behavior check missing: {', '.join(missing)}",
                "Patch routing, register, verification, artifact, or audit instructions to cover the acceptance scenario.",
                "P1",
            )
        )
    return checks


def logging_checks(root: Path, skill: str, run_id: str) -> list[Subcheck]:
    checks = [
        Subcheck(
            "test-logs/" in read_text(root / ".gitignore"),
            "test-logs ignored",
            str(root / ".gitignore"),
            "Generated logs are not ignored by Git.",
            "Add test-logs/ to .gitignore.",
            "P2",
        ),
        Subcheck(
            bool(LOG_FIELDS),
            "log schema defined",
            ", ".join(LOG_FIELDS),
            "Log schema is missing.",
            "Restore LOG_FIELDS in the harness.",
            "P3",
        ),
        Subcheck(
            True,
            "run id assigned",
            run_id,
            "Run id was not assigned.",
            "Ensure the harness creates a timestamped run id.",
            "P3",
        ),
    ]
    return checks


def skill_results(root: Path, skill: str, run_id: str, commit: str) -> list[TestResult]:
    checks_by_dimension = {
        "structural_validity": structural_checks(root, skill),
        "trigger_metadata": metadata_checks(root, skill),
        "reference_integrity": reference_checks(root, skill),
        "cognitive_contract_compliance": cognitive_checks(root, skill),
        "behavioral_routing": behavior_checks(root, skill),
        "logging_and_auditability": logging_checks(root, skill, run_id),
    }
    return [
        mk_result(
            run_id,
            commit,
            skill,
            f"{skill}.{dimension}",
            dimension,
            subchecks,
            root,
        )
        for dimension, subchecks in checks_by_dimension.items()
    ]


def summarize(results: list[TestResult]) -> tuple[dict[str, float], float]:
    by_skill: dict[str, list[TestResult]] = {}
    for result in results:
        by_skill.setdefault(result.skill, []).append(result)
    scores = {}
    for skill, rows in by_skill.items():
        earned = sum(row.points_earned for row in rows)
        possible = sum(row.points_possible for row in rows)
        scores[skill] = round((earned / possible) * 100, 2) if possible else 0.0
    suite_earned = sum(row.points_earned for row in results)
    suite_possible = sum(row.points_possible for row in results)
    suite = round((suite_earned / suite_possible) * 100, 2) if suite_possible else 0.0
    return scores, suite


def write_reports(root: Path, run_id: str, commit: str, results: list[TestResult]) -> dict[str, Path]:
    outdir = root / "test-logs" / run_id
    outdir.mkdir(parents=True, exist_ok=True)
    scores, suite = summarize(results)
    remediation = [asdict(row) for row in results if row.result != "pass"]
    payload = {
        "run_id": run_id,
        "commit": commit,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "suite_success_percent": suite,
        "skill_success_percent": scores,
        "results": [asdict(row) for row in results],
        "remediation_queue": remediation,
    }
    json_path = outdir / "report.json"
    csv_path = outdir / "report.csv"
    md_path = outdir / "report.md"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=LOG_FIELDS)
        writer.writeheader()
        writer.writerows(asdict(row) for row in results)
    lines = [
        "# Krass Skill Suite Test Report",
        "",
        f"| Field | Value |",
        f"|---|---|",
        f"| Run ID | `{run_id}` |",
        f"| Commit | `{commit}` |",
        f"| Suite Success | `{suite:.2f}%` |",
        f"| Remediation Items | `{len(remediation)}` |",
        "",
        "## Skill Scores",
        "",
        "| Skill | Success | Status |",
        "|---|---:|---|",
    ]
    for skill, score in sorted(scores.items()):
        if score >= 95:
            status = "Pass"
        elif score >= 85:
            status = "Pass with watch item"
        elif score >= 70:
            status = "Conditional pass"
        else:
            status = "Fail"
        lines.append(f"| `{skill}` | {score:.2f}% | {status} |")
    lines.extend(["", "## Remediation Queue", "", "| Skill | Dimension | Priority | Remediation |", "|---|---|---|---|"])
    if remediation:
        for row in remediation:
            remediation_text = str(row["remediation"]).replace("|", "\\|")
            lines.append(f"| `{row['skill']}` | `{row['dimension']}` | `{row['priority']}` | {remediation_text} |")
    else:
        lines.append("| None | None | None | No remediation required. |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"json": json_path, "csv": csv_path, "markdown": md_path}


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    run_id = args.run_id or datetime.now().strftime("%Y%m%d-%H%M%S")
    commit = git_commit(root)
    selected = args.skill or SKILLS
    results: list[TestResult] = []
    for skill in selected:
        results.extend(skill_results(root, skill, run_id, commit))
    paths = write_reports(root, run_id, commit, results)
    scores, suite = summarize(results)
    print(f"Run ID: {run_id}")
    print(f"Commit: {commit}")
    print(f"Suite success: {suite:.2f}%")
    for skill, score in sorted(scores.items()):
        print(f"{skill}: {score:.2f}%")
    failures = [row for row in results if row.result != "pass"]
    print(f"Remediation items: {len(failures)}")
    print(f"JSON: {paths['json']}")
    print(f"CSV: {paths['csv']}")
    print(f"Markdown: {paths['markdown']}")
    return 1 if any(row.result == "fail" for row in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
