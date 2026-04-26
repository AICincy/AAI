---
name: krass-communication-calibrator
description: Drafts, rewrites, edits, and hardens communications for Krass using recipient-specific posture, adversarial precision, statutory register, collegial directness, or natural personal voice. Use for emails, letters, complaints, regulator communications, ADA communications, professional replies, legal-adjacent correspondence, and tone corrections.
---

# Krass Communication Calibrator

## Use

Produce communications in Krass's calibrated register without softening substance, adding boilerplate, or explaining obvious context.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\register_matrix.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\confidence_summary.md` for substantive deliverables.
- Read `references/recipient_posture.md`.
- Read `references/drafting_constraints.md`.

## Procedure

- Identify recipient class, power relationship, desired action, and evidence posture.
- If the matter references prior medical, legal, provider, financial, transit, or case facts, route through `krass-context-loader` before drafting.
- If the communication includes factual claims, deadlines, citations, provider status, transit data, costs, or legal references, route through `krass-constraint-verifier` before finalizing.
- Draft in the appropriate register: statutory authority, adversarial precision, collegial directness, or natural voice.
- Preserve one objective and one requested action unless the user explicitly asks for a multi-issue document.
- Strip hedging, filler, apologies, motivational phrasing, and generic civility padding.

## Output Rules

- Provide the finished communication first.
- Include a compact confidence summary for substantive or factual communications.
- Do not include a tutorial, rationale, or writing lesson unless explicitly requested.
