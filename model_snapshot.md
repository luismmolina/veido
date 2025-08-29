# Restaurant Creator Network — Model Snapshot (Numbers)

## Core Assumptions (Locked)
- Price per restaurant (Standard): 3,600 MXN / month
- Marketing budget (fixed): 5,000 MXN / month (trackable ads)
- Creator cost: 2,000 MXN / restaurant / month
- Terms: month-to-month, no refunds
- Growth plan: Month 1 = 10, Month 2 = 20, Month 3 = 30, Month 4+ = 40

## Unit Economics (Formulas)
- Per-restaurant marketing allocation = 5,000 / N
- Per-restaurant contribution = 3,600 − 2,000 − (5,000 / N)
- Total revenue = 3,600 × N
- Total creator costs = 2,000 × N
- Total profit (pre-overhead) = N × (3,600 − 2,000) − 5,000 = 1,600 × N − 5,000
- CAC (ads-only proxy) = 5,000 / N

Notes:
- These are pre-overhead and exclude non-creator operating costs (staff, tools, payment fees, taxes).
- Marketing budget is pooled; allocation per restaurant shrinks as N grows.

## Month 1 Target Snapshot (N = 20)
- CAC (ads-only): 5,000 / 20 = 250 MXN
- Per-restaurant marketing allocation: 250 MXN
- Per-restaurant contribution: 3,600 − 2,000 − 250 = 1,350 MXN
- Total revenue: 3,600 × 20 = 72,000 MXN
- Total creator costs: 2,000 × 20 = 40,000 MXN
- Total profit (pre-overhead): 27,000 MXN
- Content volume: 20 videos/restaurant/month → 400 videos/month at 20 restaurants

## Packages (New)
- Lite: 3,300 MXN/month; no promotion; excluded from charts/top listings.
- Standard: 3,600 MXN/month; included in charts; receives promotion from pooled ads.
- Pro: 4,100 MXN/month; included in charts; extra promotion beyond Standard.

Creator work: currently modeled at 20 videos/restaurant/month with creator cost of 2,000 MXN/restaurant for all tiers (adjustable if Lite/Pro change deliverables).

Ad allocation rule (initial): Only Standard and Pro share the 5,000 MXN ad pool. Define weights to give Pro extra share.
- Weight_Standard = 1
- Weight_Pro = 2 (assumption; configurable)
- Total_shares = (count_Standard × 1) + (count_Pro × 2)
- Marketing per Standard = 5,000 × 1 ÷ Total_shares
- Marketing per Pro = 5,000 × 2 ÷ Total_shares
- Marketing per Lite = 0

Per-restaurant contribution by tier (formulas):
- Lite = 3,300 − 2,000 − 0
- Standard = 3,600 − 2,000 − Marketing per Standard
- Pro = 4,100 − 2,000 − Marketing per Pro

Illustrative example (N = 20; 10 Standard, 10 Pro; weights 1:2):
- Total_shares = 10×1 + 10×2 = 30
- Marketing/Standard = 5,000 × 1/30 = 166.67 → Contribution ≈ 1,433.33
- Marketing/Pro = 5,000 × 2/30 = 333.33 → Contribution ≈ 1,766.67

Note: Provide expected tier mix to compute exact totals; Lite has no ad cost and contributes 1,300 MXN under current creator cost.

## Ramp Forecast (Standard-only scenario)
Using Standard pricing and pooled marketing across all active Standard clients.

| Month | Restaurants (N) | Revenue (MXN) | Creator Costs (MXN) | Profit (MXN) |
|---:|---:|---:|---:|---:|
| 1 | 10 | 36,000 | 20,000 | 11,000 |
| 2 | 20 | 72,000 | 40,000 | 27,000 |
| 3 | 30 | 108,000 | 60,000 | 43,000 |
| 4+ | 40 | 144,000 | 80,000 | 59,000 |

## Sensitivity Table

| Restaurants (N) | Marketing/Restaurant (MXN) | Contribution/Restaurant (MXN) | Total Revenue (MXN) | Total Creator Costs (MXN) | Total Profit (MXN) |
|---:|---:|---:|---:|---:|---:|
| 5  | 1,000.00 | 600.00  | 18,000 | 10,000 | 3,000  |
| 10 | 500.00   | 1,100.00| 36,000 | 20,000 | 11,000 |
| 15 | 333.33   | 1,266.67| 54,000 | 30,000 | 19,000 |
| 20 | 250.00   | 1,350.00| 72,000 | 40,000 | 27,000 |
| 25 | 200.00   | 1,400.00| 90,000 | 50,000 | 35,000 |
| 30 | 166.67   | 1,433.33| 108,000| 60,000 | 43,000 |
| 40 | 125.00   | 1,475.00| 144,000| 80,000 | 59,000 |
| 50 | 100.00   | 1,500.00| 180,000| 100,000| 75,000 |
| 60 | 83.33    | 1,516.67| 216,000| 120,000| 91,000 |
| 80 | 62.50    | 1,537.50| 288,000| 160,000| 123,000|

## Tracking & Guarantees (Current Direction)
- Ads are trackable (UTM/QR per restaurant) — weekly reporting planned.
- Guarantee concept under consideration (e.g., impressions floor or make-good videos). Numbers TBD.

## Open Variables (Not Yet Set)
- Retention/churn: unknown — LTV (contribution) = monthly contribution × months retained.
- Lite/Pro tiers: concept approved; pricing and creator pay TBD.

## Related File
- `financial_model.csv` — same sensitivity data in CSV form for spreadsheet use.
