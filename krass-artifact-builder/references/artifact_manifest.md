# Artifact Manifest

## Manifest Fields

| Field | Required | Purpose |
|---|---:|---|
| `artifact_type` | Yes | File or deliverable class. |
| `output_path` | Yes | Absolute path. |
| `source_inputs` | Yes | Prompts, files, connector data, web sources, or user-provided material. |
| `generator` | Yes | Skill, plugin, script, or tool used. |
| `validation` | Yes | Checks performed and results. |
| `accessibility_gate` | Conditional | WCAG-informed cognitive-accessibility checks. |
| `source_ledger` | Conditional | Evidence provenance for factual artifacts. |
| `reuse_path` | Conditional | How the artifact can be updated or regenerated. |
| `privacy_review` | Conditional | Sensitive facts included, omitted, or redacted. |
| `residual_risk` | Yes | Remaining content, file, or source risk. |

## Manifest Rule

Do not create a persistent substantive artifact without enough manifest data to rerun, validate, or audit it later.
