# Routing Workflow

## Decision Surface

| Step | Action | Output |
|---|---|---|
| 1 | Identify the primary objective from the latest user message. | `primary_objective` |
| 2 | Classify mode using the shared mode routing table. | `mode` |
| 3 | Apply the cognitive-interface contract. | `cognitive_contract_applied: true` |
| 4 | Identify hard constraints: cost, transit, insurance, legal, medical, artifact, source, privacy. | `constraints` |
| 5 | Select downstream skill path. | `handoff_notes.route` |
| 6 | Mark verification and artifact requirements. | `verification_required`, `artifact_required` |
| 7 | Execute the route without narrating mechanics. | Draft, recommendation, file, review, or chat output |

## Default Route Patterns

| Trigger | Route |
|---|---|
| Personal profile or preference applies | `krass-cognitive-router` |
| Prior case context matters | `krass-context-loader` before output |
| Current facts or citations matter | `krass-constraint-verifier` before final claim |
| Communication output requested | `krass-communication-calibrator` |
| File or persistent artifact requested | `krass-artifact-builder` |
| Substantive output ready | `krass-quality-auditor` |

## Failure Controls

- If multiple routes apply, use dependency order: context, verification, creation, audit.
- If the user asks to execute, execute unless external permissions or missing facts block safe completion.
- If a chosen route fails, state the inaccuracy or blocker, cause, impact, and remediation plan.
