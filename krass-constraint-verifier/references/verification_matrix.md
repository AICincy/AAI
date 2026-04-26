# Verification Matrix

## Claim Classes

| Claim Type | Verification Source | Required Before Output |
|---|---|---|
| Legal citation, statute, regulation, policy | Official legal, agency, institutional, or policy source | Any citation or legal assertion |
| Medical provider, insurance, facility, hours | Official provider, payer directory, facility site, or direct listing | Any provider recommendation |
| Transit route, schedule, accessibility, fare | Official transit agency source | Any local route recommendation |
| Cost, fee, price, subscription, filing cost | Official vendor, agency, or provider source | Any financial recommendation |
| Technical API, library, product behavior | Official documentation or source repository | Any implementation guidance |
| News, leadership, current events | Recent primary or reputable reporting | Any current factual claim |
| Local business or service | Official site, directory, map listing, or agency source | Any local recommendation |
| Codex, skills, plugins, or model behavior | Official OpenAI documentation and local installed files | Any current OpenAI product or skill-system claim |
| Evidence provenance | Original artifact, official source, preserved capture, or source ledger | Any disputed or high-risk factual assertion |

## Verification Output

| Field | Content |
|---|---|
| Checked constraints | What was verified |
| Sources | URLs, documents, files, or tools |
| Gaps | What could not be verified |
| Decision impact | Whether the gap changes the recommendation |
| Confidence | High, medium, or low with reason |
| Source ledger | Claim, source URL, capture date, authority rank, volatility, contradiction status |
| Evidence grade | Primary, official secondary, corroborated, single-source, or unverified |

## Source Discipline

- Use web search automatically for volatile data.
- Use official sources first.
- Use secondary sources only when primary sources are unavailable and the limitation is stated.
- Do not include unverifiable claims for decorative authority.
- Preserve contradiction status when official sources disagree or when a directory conflicts with direct provider information.
- Treat current OpenAI product behavior, provider networks, route schedules, fares, and pricing as volatile unless a durable source proves otherwise.
