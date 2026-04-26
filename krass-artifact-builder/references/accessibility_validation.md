# Accessibility Validation

## Artifact Gates

| Artifact | Gate |
|---|---|
| Document | Stable headings, meaningful labels, table structure, explicit next action, no unnecessary cognitive load. |
| Spreadsheet | Clear sheet names, frozen headers when appropriate, validation notes, formula transparency, no hidden critical state. |
| Presentation | Consistent layouts, readable text, stable section labels, no decorative clutter that obscures state. |
| Dashboard or app | Keyboard path, text fit, visible state, predictable controls, consistent help, error recovery. |
| Form | Redundant-entry avoidance, labels, recovery path, saved user input when feasible. |
| PDF | Source artifact retained when editing is likely; render or inspect if possible. |

## WCAG-Informed Checks

- Check consistent help when help exists.
- Avoid redundant entry when prior data can be reused.
- Avoid accessible-authentication friction in workflows that include login or identity checks.
- Preserve predictable structure and explicit state labels.
- Identify residual barriers in the confidence summary.
