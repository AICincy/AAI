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
handoff_notes: {}
confidence_summary:
  sources: []
  assumptions: []
  uncertainty: []
  limits: []
```
