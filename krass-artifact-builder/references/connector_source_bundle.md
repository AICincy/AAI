# Connector Source Bundle

## Use

Apply when an artifact depends on Gmail, Google Drive, GitHub, web sources, local files, or other connected data.

## Bundle Fields

| Field | Purpose |
|---|---|
| `source_id` | Connector id, URL, commit hash, message id, file path, or document id. |
| `source_type` | Gmail, Drive, GitHub, web, local file, generated asset, or user prompt. |
| `capture_date` | Date checked or exported. |
| `use_in_artifact` | What the source supports. |
| `privacy_class` | Ordinary, personal, medical, legal, financial, credential, or sensitive. |
| `retention` | Keep, omit, redact, or archive. |

## Rules

- Prefer connector readback over screenshots when structured content is available.
- Do not publish source bundles by default.
- Keep generated logs and bundles local unless Krass explicitly requests external publication.
