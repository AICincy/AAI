# Router Trace

## Current Synthesis

Routing should be deterministic, inspectable, and quiet. Maintain an internal trace unless exposing it improves auditability or remediation.

## Trace Fields

| Field | Purpose |
|---|---|
| `mode` | Classified task mode. |
| `mode_confidence` | High, medium, or low confidence in the classification. |
| `primary_objective` | Single objective controlling downstream work. |
| `risk_tier` | Ordinary, elevated, high, or critical. |
| `dependency_graph` | Ordered skill path with blockers and prerequisites. |
| `plugin_or_skill` | Plugin for connected data; skill for repeatable process. |
| `recency_requirement` | Live, current cycle, annual, durable, or historical. |
| `public_trace` | Whether the trace should be exposed in the final output. |

## Plugin vs Skill Selection

| Need | Route |
|---|---|
| Connected account data, email, Drive, GitHub, web, current provider, or transit data | Plugin or web source |
| Krass-specific output architecture, drafting posture, constraint gates, artifact policy, or audit rubric | Skill |
| Both connected information and Krass-specific process | Plugin first for data, skill second for process |

## Trace Rule

Expose a router trace only when the output is high-risk, the route is disputed, the user asks for auditability, or remediation requires it.
