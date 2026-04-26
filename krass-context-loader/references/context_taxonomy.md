# Context Taxonomy

## Fact Classes

| Class | Examples | Handling |
|---|---|---|
| Identity and role | Professional titles, academic background, licensure, faculty status | Use only when it changes register, authority, or artifact framing |
| Cognitive interface | AuDHD architecture, pattern compression, monotropic focus, asymmetric working memory | Apply globally to output structure |
| Medical | Conditions, providers, facility assessments, insurance constraints | Load before healthcare output; avoid unnecessary disclosure |
| Legal | Cases, opposing parties, regulators, filings, deadlines, evidence | Load before legal-adjacent drafting or review |
| Financial | Account status, cost limits, funding constraints | Load before recommendations with expense implications |
| Transit and geography | Deer Park, Hamilton County, Metro, MetroNow, Metro Access | Load before local recommendations |
| Prior work | Drafts, artifacts, decisions, corrections, preferences | Load before continuing or revising |
| Facility and provider relationships | Approved, excluded, failed, pending, or preferred entities | Load before naming options |

## State Labels

| Label | Meaning |
|---|---|
| Known | Explicitly present in memory, conversation, file, or source |
| Inferred | Reasonable from context but not directly stated |
| Stale | Previously known but likely changed |
| Missing | Needed for safe output and not discoverable |
| Sensitive | Should not be exposed unless required |

## Context Packet

```yaml
known_facts: []
inferred_facts: []
stale_facts: []
missing_facts: []
sensitive_facts: []
impact_on_output: []
```
