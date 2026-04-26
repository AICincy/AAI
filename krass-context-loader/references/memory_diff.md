# Memory Diff

## Use

Apply when a new request conflicts with prior context, updates a constraint, or asks to continue prior work.

## Diff Fields

| Field | Purpose |
|---|---|
| `prior_fact` | Previous fact or assumption. |
| `new_fact` | New or corrected fact. |
| `status` | Confirmed, inferred, superseded, disputed, or stale. |
| `source` | Conversation, memory, file, connector, or web source. |
| `impact` | How the change affects the output. |
| `action` | Use, omit, verify, ask, or preserve. |

## Conflict Rule

Use the newest user correction as controlling unless it conflicts with verified external constraints or safety-critical facts.
