# Veido — Restaurant Creator Network (Modeling Snapshot)

A lightweight model for a citywide restaurant content + promotion network.

- Restaurants pay monthly for short-form video content; Standard/Pro tiers include distribution via city channels and paid promotion.
- Creators are paid per accepted video following clear guidelines.
- Upfront billing (100%) and minimal overhead enable early positive cash flow.

## Packages
- Lite: 3,300 MXN/month — videos only, no charts/promotion.
- Standard: 3,600 MXN/month — videos + eligibility for charts + shared promotion.
- Pro: 4,100 MXN/month — Standard plus extra promotion.

Notes
- Creator cost (all tiers, current model): 2,000 MXN/restaurant/month (20 videos assumed).
- Ads budget (fixed): 5,000 MXN/month, allocated only across Standard/Pro.
- Ad allocation weights: Standard = 1, Pro = 2 (configurable).

## Growth Plan
- Month 1 = 10 restaurants
- Month 2 = 20
- Month 3 = 30
- Month 4+ = 40

## Files
- model_snapshot.md: Core assumptions, formulas, sensitivity table, and tier logic.
- projections.csv: Tiered monthly projections and recurring profit.
- startup_projection.csv: Cash flow with upfront billing, payment fees, tools, and legal one-time.
- assumptions.csv: Central inputs (prices, costs, growth targets, ad weights).
- financial_model.csv: Sensitivity of per-restaurant economics vs number of clients.

## How to Read projections.csv
Columns
- Revenue_MXN: Monthly billing by tier mix (Lite/Standard/Pro).
- Creator_Costs_MXN: 2,000 × total restaurants (current assumption; change if deliverables differ by tier).
- Marketing_Budget_MXN: Fixed 5,000 MXN/month.
- Shares: Ad allocation denominator = Standard_count × 1 + Pro_count × 2.
- Marketing_per_Standard_MXN, Marketing_per_Pro_MXN: Per-restaurant ad allocation under weights.
- Contribution_per_[Tier]_MXN: Price − creator cost − allocated marketing (Lite has no marketing).
- Profit_MXN: Revenue − creator costs − marketing (pre-fees/overhead).
- Monthly_Recurring_Profit_MXN: Same as Profit_MXN for clarity (recurring contribution before fees/overhead).

## How to Read startup_projection.csv
Assumptions
- Payment_Fees_MXN: 3.5% of revenue (stripe-like proxy).
- Software_Tools_MXN: 1,500 MXN/month.
- Domain/Hosting: 0 MXN/month (using free hosting like Vercel).
- Legal_Admin_OneTime_MXN: 6,000 MXN in Month 0.

Columns
- Net_Cash_In_MXN: Revenue − payment fees (reflects upfront billing).
- Net_Cash_Flow_MXN: Net cash in − ads − creator − tools − one-time where applicable.
- Cumulative_Cash_MXN: Running total of cash after expenses.
- Monthly_Recurring_Profit_MXN: Net cash in − ads − creator − tools (excludes one-time items).

## Tracking & Guarantees (Direction)
- Trackable ads via UTM/QR per restaurant; weekly reporting.
- Guarantee concept: make-good on deliverables and/or impressions floor (TBD).

## Next Steps
- Confirm creator deliverables by tier (e.g., Lite 10–12 videos; Pro 20 + edits) and adjust creator costs accordingly.
- Lock tier mix targets per month to refine projections.
- Optional: Convert these models into a Google Sheet with formulas and charts.

---
Questions or updates to assumptions? Edit assumptions.csv and open an issue/PR, or ask to regenerate the projections with new inputs.
