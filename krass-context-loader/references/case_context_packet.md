# Case Context Packet

## Packet

```yaml
case_context_packet:
  primary_objective: ""
  durable_facts: []
  volatile_facts: []
  sensitive_facts: []
  superseded_facts: []
  disputed_facts: []
  source_history: []
  privacy_minimization:
    used: []
    omitted: []
    redacted: []
  verification_needed: []
  impact_on_output: []
```

## Rules

- Do not expose the packet unless auditability or remediation requires it.
- Use the packet to prevent context amnesia and over-disclosure.
- Route volatile or disputed facts to `krass-constraint-verifier`.
