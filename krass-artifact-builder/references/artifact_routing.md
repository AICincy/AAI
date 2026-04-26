# Artifact Routing

## Route Table

| Artifact Type | Preferred Skill or Tooling | Required Validation |
|---|---|---|
| DOCX or document | `documents:documents` skill when available | Render or inspect with the document workflow |
| XLSX, CSV, TSV, spreadsheet | `spreadsheets:Spreadsheets` skill when available | Formula, structure, and file integrity check |
| PPTX or slide deck | `presentations:Presentations` skill when available | Render or export validation |
| React, frontend app, dashboard, game | `build-web-apps:frontend-app-builder` plus relevant frontend skills | Local dev server and browser or screenshot verification |
| Image asset | `imagegen` skill when bitmap generation or editing is appropriate | Visual inspection |
| Markdown or text artifact | Native file creation | Readback and content check |
| PDF | Relevant document, browser, or PDF workflow | Open, render, or inspect where feasible |
| GitHub publication | GitHub plugin skills when user asks to publish | Branch, commit, push, and PR verification |
| Source bundle or audit package | Native filesystem plus connector exports where available | Manifest, source ledger, and privacy review |

## Artifact Packet

| Field | Content |
|---|---|
| artifact_type | File or deliverable class |
| output_path | Absolute path |
| source_inputs | Files, prompts, data, or links used |
| generator | Skill, tool, or script used |
| validation | Check performed and result |
| residual_risk | Remaining file or content risk |
| accessibility_gate | WCAG-informed cognitive-accessibility checks |
| source_bundle | Connector files, URLs, captures, or source ledger entries |

## Execution Rule

Create the requested file when the user asks for a deliverable. Do not stop at instructions unless blocked by missing input, permissions, or unavailable tooling.
