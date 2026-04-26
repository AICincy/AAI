# Evidence Provenance Contract

## Current Synthesis

Evidence quality is a control surface. Every volatile, legal, medical, financial, local, policy, technical, or public-facing claim needs a source ledger before it is used as authority.

## Source Ledger

| Field | Required | Purpose |
|---|---:|---|
| `claim` | Yes | State the exact assertion being supported. |
| `source_url` | Yes | Record the canonical URL or local file path. |
| `source_title` | Yes | Identify the source without relying on link text alone. |
| `publisher` | Yes | Identify the responsible entity. |
| `capture_date` | Yes | Use the date the source was checked. |
| `authority_rank` | Yes | Mark primary, official secondary, reputable secondary, user-generated, or unknown. |
| `volatility` | Yes | Mark live, current cycle, annual, durable, or historical. |
| `contradiction_status` | Yes | Mark none found, unresolved, or contradicted. |
| `preservation_need` | Yes | Mark none, screenshot, PDF, archived copy, or evidentiary bundle. |
| `use_limit` | Yes | State what the source can and cannot prove. |

## Authority Ranking

| Rank | Use |
|---|---|
| Primary | Official source that controls the fact, such as statute, agency page, payer directory, vendor documentation, transit agency data, court record, or original artifact. |
| Official secondary | Official explanatory source that interprets or summarizes controlling material. |
| Reputable secondary | Established reporting, institutional analysis, or domain documentation when primary sources are unavailable. |
| User-generated | Reddit, forums, comments, social posts, or reviews; use only as anecdotal signal or lead generation. |
| Unknown | Do not rely on the claim without additional support. |

## Contradiction Handling

- Prefer primary sources over secondary sources.
- If two primary sources conflict, mark `contradiction_status: unresolved` and avoid a definitive claim.
- If a directory lists a provider but the provider site contradicts it, require direct confirmation or state the conflict.
- Preserve source captures for legal, medical, financial, provider, or adversarial communications when the claim may later be disputed.

## Source-Grounded Defaults

| Domain | Default Source |
|---|---|
| Codex and skills behavior | Official OpenAI documentation or local installed skill files |
| ADA communication posture | ADA.gov and controlling statute or regulation when needed |
| Cognitive accessibility | W3C WCAG 2.2 Understanding and relevant normative WCAG text |
| Cincinnati transit | Metro official pages, GTFS data, and GTFS Realtime reference |
| CareSource provider status | CareSource Find A Doctor/Provider, provider portal, or member/provider documents |
| OSINT and preservation | Berkeley Protocol and primary digital artifacts |
