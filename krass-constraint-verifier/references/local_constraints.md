# Local Constraints

## Standing Constraints

| Domain | Constraint | Verification Requirement |
|---|---|---|
| Geography | Deer Park, Ohio and Hamilton County region | Verify exact address, distance, and service area before recommending |
| Transit | Public transit focus: Metro routes 4, 5, MetroNow, Metro Access | Verify current route, stop, schedule, eligibility, and fare details |
| Mobility | No private vehicle or rideshare assumption | Do not recommend car-dependent options unless user explicitly changes constraint |
| Insurance | CareSource Medicaid provider verification required | Verify payer acceptance through current source before provider recommendation |
| Financial | Economic constraints persist when stated | Prefer no-cost or lowest-cost options and verify fees |
| Medical | Known conditions and provider relationships may matter | Load available context before healthcare output |
| Facility exclusions | Prior facility assessments may control recommendations | Check available context before naming facilities |

## Local Recommendation Gate

Do not deliver a local recommendation until these fields are checked or explicitly marked unavailable:

| Field | Required State |
|---|---|
| Address | Verified |
| Transit access | Verified or unavailable |
| Cost exposure | Verified or unavailable |
| Insurance acceptance | Verified or unavailable |
| Hours or availability | Verified or unavailable |
| Source date | Current enough for the claim |

## Transit Standard

Transit-accessible means the option can be reached without private vehicle or rideshare under the user's practical constraints. A nominal route existing nearby is insufficient when schedule, walk distance, accessibility, fare, or service boundary makes the option impractical.
