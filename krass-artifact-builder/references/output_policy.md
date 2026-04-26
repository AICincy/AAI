# Output Policy

## Path Resolution

| Priority | Destination |
|---|---|
| 1 | Explicit path supplied by the user |
| 2 | `/mnt/user-data/outputs/` when available |
| 3 | Workspace `outputs/` directory when `/mnt/user-data/outputs/` is unavailable |
| 4 | Current working directory only for trivial local artifacts |

## File Rules

- Use absolute paths in final responses.
- Create parent directories when needed.
- Avoid overwriting existing files unless the user requested replacement or the file is part of the current task.
- Preserve unrelated user files and uncommitted changes.
- Validate created files through the relevant domain workflow.

## Final Response

Include:

| Field | Requirement |
|---|---|
| Path | Absolute path to each artifact |
| Validation | Command, render, readback, or inspection performed |
| Caveat | Any missing input, unavailable tooling, or unverified claim |
| Confidence | Summary required for substantive artifacts |
