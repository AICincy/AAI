---
name: krass-cognitive-router
description: Routes Krass personal Codex workflows through shared cognitive-interface and mode-routing contracts. Use for any request that invokes Krass preferences, AuDHD support requirements, personal workflow rules, Continue behavior, drafting, verification, artifact creation, review, or coordination among Krass skill suite skills.
---

# Krass Cognitive Router

## Use

Classify the request, enforce the cognitive-interface contract, and create a compact task packet before any specialized execution.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\handoff_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\mode_routing.md`.
- Read `references/routing_workflow.md`.

## Routing Procedure

- Infer the mode from natural language; do not ask when the route is inferable.
- Generate an internal `task_packet` with objective, constraints, mode, downstream skill path, verification flag, artifact flag, and confidence requirements.
- Route case-specific, medical, legal, provider, financial, transit, or prior-work tasks through `krass-context-loader` before drafting or recommendation.
- Route volatile factual claims, local recommendations, costs, citations, insurance, or transit feasibility through `krass-constraint-verifier`.
- Route communications through `krass-communication-calibrator`.
- Route file deliverables through `krass-artifact-builder`.
- Route substantive final outputs through `krass-quality-auditor`.
- For `Continue`, resume from the last active artifact or reasoning state without recap.

## Output Rules

- Lead with synthesis, confidence level, and falsification criteria for substantive deliverables.
- Use tables as the default comparison and state-mapping format.
- Maintain senior-level register and omit pedagogical scaffolding.
- Keep secondary issues in a parking lot only when they matter and do not interrupt the primary objective.
