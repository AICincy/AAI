---
name: krass-quality-auditor
description: Audits Krass deliverables before final output for cognitive-interface compliance, senior register, factual support, verification gaps, source ledgers, risk governance, accessibility gates, reversibility, scope control, failure modes, omitted constraints, artifact validity, remediation severity, and confidence-summary completeness.
---

# Krass Quality Auditor

## Use

Pressure-test substantive outputs before final response. Treat the audit as an execution gate, not commentary.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\confidence_summary.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\risk_governance_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\evidence_provenance_contract.md` when claims or sources are present.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\accessibility_contract.md` for artifacts or workflows.
- Read `references/audit_matrix.md`.
- Read `references/failure_modes.md`.
- Read `references/risk_governance_audit.md`.
- Read `references/red_team_prompt_suite.md`.
- Read `references/remediation_severity.md`.

## Procedure

- Verify the output preserves one primary objective and one next action.
- Check for deficit framing, pedagogical scaffolding, generic hedging, unsupported factual claims, and stale constraints.
- Confirm that current claims, citations, costs, insurance, transit, provider status, and legal references were verified when required.
- Confirm source ledger, evidence grade, risk tier, accessibility gate, privacy minimization, and remediation status when applicable.
- Check reversibility and identify irreversible or externally persistent actions.
- Revise the deliverable directly when defects are correctable.
- Block or explicitly qualify claims that cannot be supported.

## Output Rules

- Do not expose the audit trail unless it adds value to the user's deliverable.
- Append the confidence summary for substantive work.
- Omit the confidence summary for casual chat, short answers, and self-evident command outputs.
