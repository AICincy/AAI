---
name: krass-core-contracts
description: Shared reference contracts for Krass personal Codex workflows. Use when Codex needs the AuDHD cognitive-interface contract, task handoff schema, mode routing rules, recipient register matrix, confidence-summary protocol, evidence provenance, risk governance, source aging, or cognitive-accessibility gates before executing Krass-specific work.
---

# Krass Core Contracts

## Use

Load this skill as the shared source of truth for Krass-specific execution. Use it to align downstream skills without duplicating large preference blocks.

## Reference Loading

| Need | Read |
|---|---|
| Cognitive-interface and output architecture | `references/cognitive_interface_contract.md` |
| Silent coordination between skills | `references/handoff_contract.md` |
| Natural-language mode classification | `references/mode_routing.md` |
| Confidence summary requirements | `references/confidence_summary.md` |
| Recipient register and communication posture | `references/register_matrix.md` |
| Source ledger, capture, contradiction, and preservation rules | `references/evidence_provenance_contract.md` |
| Risk tiers, review gates, and NIST-style governance mapping | `references/risk_governance_contract.md` |
| Cognitive-accessibility gates for artifacts, forms, and workflows | `references/accessibility_contract.md` |

## Operating Rules

- Treat AuDHD as an information-processing architecture, not a deficit category.
- Preserve one primary objective, one active thread, and one next action.
- Prefer compressed synthesis, tables, explicit state labels, and verification surfaces.
- Avoid introductory explanation, motivational padding, remedial language, and generic hedging.
- Keep shared contracts authoritative; downstream skills should reference them instead of restating them.
- Expose handoff packets only when they improve the final deliverable.
- Use provenance, risk, and accessibility contracts for high-stakes, persistent, public, legal, medical, financial, local, or artifact outputs.
