# Risk Governance Contract

## Current Synthesis

High-stakes outputs need governance, not just quality review. Use the Govern, Map, Measure, Manage pattern to convert ambiguous risk into explicit gates, evidence, and remediation.

## Risk Tiers

| Tier | Criteria | Required Gate |
|---|---|---|
| Ordinary | Low consequence, reversible, no external claim dependency | Normal skill execution |
| Elevated | Persistent artifact, professional communication, or moderate factual dependence | Source ledger and quality audit |
| High | Legal, medical, financial, provider, transit, institutional, regulatory, or adversarial consequence | Context loader, constraint verifier, risk audit, confidence summary |
| Critical | Irreversible external action, filing, complaint, payment, health decision, public allegation, or safety implication | Explicit risk packet, source ledger, remediation path, and user-visible uncertainty |

## Governance Map

| Function | Skill Responsibility |
|---|---|
| Govern | Define policy, constraints, privacy, source authority, and review gates. |
| Map | Identify stakeholders, context, claims, affected systems, and failure modes. |
| Measure | Run validators, harness checks, source verification, artifact inspection, and contradiction scans. |
| Manage | Prioritize remediation, define owner, state retest command, and document residual risk. |

## Risk Packet

```yaml
risk_tier: elevated
govern:
  policy_constraints: []
  privacy_constraints: []
map:
  stakeholders: []
  affected_systems: []
  claims: []
measure:
  tests: []
  source_ledger: []
  failed_gates: []
manage:
  remediation: []
  residual_risk: []
  retest_command: ""
```

## Escalation Rules

- Raise risk tier when a claim affects access to care, legal rights, money, transit feasibility, professional standing, institutional compliance, or public record.
- Do not lower risk tier because the output is short.
- Do not publish, file, send, or persist a critical output without a visible confidence summary and residual-risk statement.
