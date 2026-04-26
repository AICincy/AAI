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
| Source ledger | Claim, URL, capture date, authority rank, and contradiction status recorded |

## Transit Standard

Transit-accessible means the option can be reached without private vehicle or rideshare under the user's practical constraints. A nominal route existing nearby is insufficient when schedule, walk distance, accessibility, fare, or service boundary makes the option impractical.

## Cincinnati Transit Distinctions

| Service | Verification Rule |
|---|---|
| Fixed-route Metro | Verify route, stop, schedule, fare, transfer, walk distance, and service date. |
| MetroNow | Verify zone, scheduled-trip requirement, fare, pass compatibility, phone/app booking path, and operating hours. |
| Metro Access | Verify eligibility requirements, booking rules, service area, fare, and whether it applies to the specific trip. |
| GTFS schedule data | Treat as schedule/trip-planning data and check feed age before relying on it. |
| GTFS Realtime | Distinguish trip updates, vehicle positions, and alerts from scheduled route availability. |

## CareSource Healthcare Gate

| Field | Requirement |
|---|---|
| Provider network | Verify through CareSource directory, provider portal, or official member/provider material. |
| New-patient status | Verify directly or mark unconfirmed. |
| Coverage fit | Confirm Medicaid, MyCare, Marketplace, or other plan type before naming the option. |
| Transportation benefit | Check when fixed-route transit is weak or appointment distance is material. |
