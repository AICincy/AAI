# Fact Aging

## Aging Model

| Fact Type | Default Age State | Recheck Trigger |
|---|---|---|
| Identity, professional role, cognitive-interface preference | Durable | User correction or new profile facts |
| Provider network, accepting-patient status, hours | Volatile | Every recommendation |
| Transit route, schedule, fare, zone, eligibility | Volatile | Every local route recommendation |
| Legal deadline, filing status, agency policy | Volatile | Every legal-adjacent output |
| Medical facility assessment or provider relationship | Current cycle | New visit, denial, referral, or correction |
| Financial constraint | Current cycle | User changes budget or task implies cost |
| Drafting preference | Durable | User tone correction |
| Source URL or citation | Current cycle | Every public or high-stakes reuse |

## Output Impact

- Durable facts may be reused unless contradicted.
- Volatile facts require verification before recommendation.
- Superseded facts must be excluded or explicitly labeled.
- Disputed facts require confidence limits and contradiction status.
