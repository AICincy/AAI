---
name: krass-context-loader
description: Loads prior and case-specific context before Krass outputs. Use when a request references prior work, medical information, provider relationships, legal matters, financial accounts, transit constraints, facility exclusions, local recommendations, source history, fact aging, memory differences, or any continuing case narrative that depends on remembered facts.
---

# Krass Context Loader

## Use

Recover relevant context before producing case-specific work. Prevent omissions caused by relying only on the newest message.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\handoff_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\evidence_provenance_contract.md` when prior sources or artifacts are material.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\risk_governance_contract.md` for high-stakes context.
- Read `references/context_taxonomy.md`.
- Read `references/fact_aging.md`.
- Read `references/memory_diff.md`.
- Read `references/case_context_packet.md`.

## Procedure

- Search available conversation history, memory surfaces, workspace files, and connected services when the active runtime provides them.
- Load only facts relevant to the current objective.
- Separate known facts, inferred facts, stale facts, and missing facts.
- Classify facts as durable, volatile, superseded, disputed, or sensitive.
- Build a memory diff when new facts conflict with prior facts.
- If a memory tool is unavailable, use visible thread context and state the limitation only if it affects confidence.
- For medical, legal, provider, financial, transit, and facility work, construct an internal `context_packet` before drafting, recommending, or deciding.
- Do not expose sensitive context unless it is necessary for the requested output.

## Output Rules

- Preserve the user's terminology and case framing.
- Avoid restating profile information unless it materially changes the deliverable.
- Route factual claims and live constraints to `krass-constraint-verifier`.
