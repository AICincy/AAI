# Handoff Contract

## Principle

Skills do not perform autonomous background messaging. Silent coordination means the active Codex instance carries compact packet state between loaded skills and shared references.

## Task Packet

| Field | Type | Required | Producer | Consumer | Purpose |
|---|---:|---:|---|---|---|
| `mode` | enum | Yes | router | all skills | Route execute, draft, decide, design, troubleshoot, summarize, review, or chat. |
| `primary_objective` | string | Yes | router | all skills | Preserve monotropic focus. |
| `cognitive_contract_applied` | boolean | Yes | router | all skills | Confirm the AuDHD architecture rules are active. |
| `constraints` | list | Yes | router, verifier, context loader | all skills | Carry non-negotiables and practical limits. |
| `audience` | string | Conditional | communication calibrator | artifact builder, auditor | Calibrate register and authority posture. |
| `verification_required` | boolean | Yes | router, verifier | verifier, auditor | Force current-source checks. |
| `artifact_required` | boolean | Yes | router | artifact builder | Determine whether a file must be created. |
| `sensitivity` | enum | Yes | context loader | all skills | Mark medical, legal, financial, personal, or ordinary context. |
| `risk_tier` | enum | Yes | router, auditor | all skills | Mark ordinary, elevated, high, or critical operational risk. |
| `source_ledger` | list | Conditional | verifier, context loader | auditor, final output | Track source URL, authority rank, capture date, volatility, and contradiction status. |
| `recency_requirement` | enum | Conditional | verifier | auditor | Mark live, current cycle, annual, durable, or historical source freshness. |
| `evidence_grade` | enum | Conditional | verifier, auditor | communication calibrator, auditor | Rank claim support as primary, official secondary, corroborated, single-source, or unverified. |
| `accessibility_gate` | map | Conditional | artifact builder, auditor | auditor, final output | Track WCAG-informed cognitive-accessibility checks for artifacts and workflows. |
| `privacy_minimization` | map | Conditional | context loader, auditor | all skills | Track sensitive facts used, omitted, or redacted. |
| `remediation_status` | map | Conditional | auditor | final output | Track failed gates, owner, severity, retest command, and closure state. |
| `handoff_notes` | map | Yes | all skills | next skill | Transfer compact state without public narration. |
| `confidence_summary` | map | Conditional | auditor | final output | Report sources, assumptions, uncertainty, and scope. |

## Packet Discipline

- Keep packets internal unless exposing them improves the deliverable.
- Use packets to prevent repeated preference blocks in final output.
- Update packet state after verification, context loading, artifact creation, and audit.
- Do not invent memory, sources, citations, routes, costs, or provider relationships.

## Minimal Packet Shape

```yaml
mode: execute
primary_objective: ""
cognitive_contract_applied: true
constraints: []
audience: null
verification_required: false
artifact_required: false
sensitivity: ordinary
risk_tier: ordinary
source_ledger: []
recency_requirement: durable
evidence_grade: unverified
accessibility_gate: {}
privacy_minimization: {}
remediation_status: {}
handoff_notes: {}
confidence_summary:
  sources: []
  assumptions: []
  uncertainty: []
  limits: []
```
