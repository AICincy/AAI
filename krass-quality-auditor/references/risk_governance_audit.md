# Risk Governance Audit

## Audit Rubric

| Function | Audit Question | Failure Action |
|---|---|---|
| Govern | Are policies, constraints, privacy, source authority, and review gates explicit? | Add governance packet. |
| Map | Are stakeholders, claims, systems, and failure modes identified? | Add context and risk map. |
| Measure | Are validators, source checks, artifact checks, and contradiction scans documented? | Run or request missing checks. |
| Manage | Are remediation actions prioritized with owner, retest command, and residual risk? | Add remediation status. |

## Risk Audit Packet

```yaml
risk_audit:
  risk_tier: ""
  failed_gates: []
  residual_risk: []
  remediation_status: []
  retest_command: ""
```
