---
name: krass-constraint-verifier
description: Verifies current facts and practical constraints for Krass before recommendations or factual outputs. Use for citations, URLs, legal or policy claims, costs, insurance acceptance, CareSource Medicaid, public transit, provider status, business hours, local recommendations, route feasibility, and any information with meaningful chance of recent change.
---

# Krass Constraint Verifier

## Use

Convert factual and logistical uncertainty into explicit verification work before producing recommendations, drafts, or decisions.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\handoff_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\confidence_summary.md`.
- Read `references/verification_matrix.md`.
- Read `references/local_constraints.md`.

## Procedure

- Identify every claim that is current, external, costly, medical, legal, financial, logistical, or source-sensitive.
- Use web search or the most authoritative available tool when information may have changed.
- Prefer primary sources: official agencies, provider directories, carrier sites, court or statute sources, institution pages, or vendor documentation.
- For local recommendations, verify transit access, cost exposure, hours, geography, and insurance constraints before naming options.
- Omit unverified claims when verification fails; mark only unavoidable uncertainty explicitly.
- Produce a `verification_packet` with sources, checked constraints, unresolved gaps, and confidence level.

## Output Rules

- Do not recommend a local service until practical constraints are verified.
- Do not fabricate citations, URLs, provider acceptance, route availability, or costs.
- Append a confidence summary to substantive outputs that used verification.
