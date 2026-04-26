# Mode Routing

## Routing Table

| User Intent Pattern | Mode | Primary Skill Path |
|---|---|---|
| Crash, exception, broken, exit code, error | troubleshoot | router -> verifier if external facts -> auditor |
| Draft, compose, create a message, write a letter | draft | router -> context loader if case-specific -> communication calibrator -> auditor |
| Fix, edit, rewrite, update language | rewrite | router -> communication calibrator or artifact builder -> auditor |
| Should I, compare, which option, help me choose | decide | router -> verifier if factual constraints -> auditor |
| Build, architect, design, structure | design | router -> artifact builder or specialized domain skill -> auditor |
| Summarize, TLDR, condense | summarize | router -> context loader if prior material -> auditor when substantive |
| Review, feedback, check, what do you think | review | router -> quality auditor -> calibrator if edits are required |
| Random question, curious, tell me about | chat | router only unless current facts or citations are needed |
| Continue | continue | router resumes from the last active state without recap |
| Anything else actionable | execute | router selects the inferred specialized path |

## Clarification Rule

Ask only when the next action is materially risky and the missing variable cannot be discovered from local context, available tools, or the request itself.

## Continue Rule

For `Continue`, resume the interrupted artifact, list, draft, or analysis at the point of cessation. Do not summarize the prior exchange unless the user asks for summary.
