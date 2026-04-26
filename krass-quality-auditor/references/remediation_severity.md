# Remediation Severity

## Severity Model

| Severity | Criteria | Required Action |
|---|---|---|
| P0 | Defect could cause legal, medical, financial, safety, privacy, or external-record harm | Block output or publication until fixed. |
| P1 | Skill route, source ledger, risk tier, or artifact validation fails | Patch before relying on affected skill. |
| P2 | Quality drift, missing accessibility note, weak confidence summary, or incomplete trace | Patch in next revision cycle. |
| P3 | Cleanup, wording, or nonblocking documentation issue | Track and batch with maintenance. |

## Remediation Packet

```yaml
remediation_status:
  severity: P1
  owner_skill: ""
  failed_gate: ""
  fix_action: ""
  retest_command: ""
  closure_state: open
```
