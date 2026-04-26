---
name: krass-artifact-builder
description: Creates or routes concrete deliverables for Krass. Use for markdown, HTML, React apps, DOCX, XLSX, CSV, PPTX, PDF, diagrams, dashboards, forms, templates, structured documents, artifact manifests, WCAG-informed accessibility gates, connector source bundles, and any request where the expected output is a file or persistent artifact.
---

# Krass Artifact Builder

## Use

Convert executable requests into concrete artifacts while preserving the cognitive-interface contract and using the correct specialized Codex skill or plugin.

## Required References

- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\cognitive_interface_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\handoff_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\accessibility_contract.md`.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\evidence_provenance_contract.md` when sources feed the artifact.
- Read `C:\Users\krass\.codex\skills\krass-core-contracts\references\risk_governance_contract.md` for persistent, public, legal, medical, financial, or institutional artifacts.
- Read `references/artifact_routing.md`.
- Read `references/output_policy.md`.
- Read `references/artifact_manifest.md`.
- Read `references/accessibility_validation.md`.
- Read `references/connector_source_bundle.md`.

## Procedure

- Infer artifact type from the request and select the relevant specialized skill before file creation.
- Consult the applicable `SKILL.md` for documents, spreadsheets, presentations, frontend apps, image generation, or other artifact domains.
- Use deterministic tooling for file generation and validation where available.
- Build an artifact manifest with source inputs, generator, validation checks, accessibility gate, and reuse path.
- Bundle connector or web sources when they materially shape the artifact.
- Place outputs in the user-specified path when provided; otherwise follow `references/output_policy.md`.
- Route substantive artifacts through `krass-quality-auditor` before final response.

## Output Rules

- Create the artifact instead of describing how to create it.
- Return absolute paths to generated files.
- Include validation status and confidence summary unless the artifact is trivial or self-evident.
