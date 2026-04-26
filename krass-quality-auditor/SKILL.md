---
name: krass-quality-auditor
description: Audits Krass deliverables before final output for cognitive-interface compliance, senior register, factual support, verification gaps, reversibility, scope control, failure modes, omitted constraints, artifact validity, and confidence-summary completeness.
---

# Krass Quality Auditor

## Use

Pressure-test substantive outputs before final response. Treat the audit as an execution gate, not commentary.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\confidence_summary.md`.
- Read `references/audit_matrix.md`.
- Read `references/failure_modes.md`.

## Procedure

- Verify the output preserves one primary objective and one next action.
- Check for deficit framing, pedagogical scaffolding, generic hedging, unsupported factual claims, and stale constraints.
- Confirm that current claims, citations, costs, insurance, transit, provider status, and legal references were verified when required.
- Check reversibility and identify irreversible or externally persistent actions.
- Revise the deliverable directly when defects are correctable.
- Block or explicitly qualify claims that cannot be supported.

## Output Rules

- Do not expose the audit trail unless it adds value to the user's deliverable.
- Append the confidence summary for substantive work.
- Omit the confidence summary for casual chat, short answers, and self-evident command outputs.
