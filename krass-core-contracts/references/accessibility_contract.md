# Accessibility Contract

## Current Synthesis

Cognitive accessibility is an operational requirement for artifacts, workflows, forms, dashboards, and instructions. It complements Krass's AuDHD cognitive-interface contract without reframing AuDHD as a deficit.

## WCAG-Informed Gates

| Gate | Requirement |
|---|---|
| Consistent help | Help, next actions, and recovery instructions appear predictably when present. |
| Redundant entry | Do not require repeated input when prior data can be reused, selected, or prefilled. |
| Accessible authentication awareness | Do not design workflows that rely on memory tests, transcription puzzles, or avoidable cognitive function tests. |
| Predictable structure | Preserve stable headings, labels, tables, and state labels across artifacts. |
| Error recovery | Identify errors, explain correction path, and preserve user-entered data where possible. |
| Attention control | Avoid unnecessary animation, time pressure, surprise context switches, and hidden state. |

## Artifact Accessibility Packet

```yaml
accessibility_gate:
  consistent_help: unchecked
  redundant_entry: unchecked
  authentication_friction: unchecked
  predictable_structure: unchecked
  error_recovery: unchecked
  attention_control: unchecked
  residual_barriers: []
```

## Usage

- Apply to documents, spreadsheets, slide decks, dashboards, forms, websites, and multi-step workflows.
- For communication drafts, apply predictable structure and state labeling rather than reading-level simplification.
- For dashboards or apps, test small screens, keyboard flow, visible state, and text fit when feasible.
