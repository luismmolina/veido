#!/usr/bin/env python3
# Restaurant Content Creator Network Financial Analysis

# Constants
RESTAURANTS_PER_CATEGORY = 20
MONTHLY_SUBSCRIPTION_FEE = 3600  # MXN per restaurant per month
CREATOR_COST_PER_RESTAURANT = 2000  # MXN (10 creators × 200 MXN each)
FIXED_MARKETING_BUDGET = 5000  # MXN per month

print('=== RESTAURANT CONTENT CREATOR NETWORK FINANCIAL ANALYSIS ===\n')
print('MONTHLY SUBSCRIPTION MODEL: $3,600 MXN per restaurant per month\n')

# Per Restaurant Analysis
print('PER RESTAURANT (Monthly):')
print(f'Restaurant pays: ${MONTHLY_SUBSCRIPTION_FEE:,} MXN/month')
print(f'Creator costs: ${CREATOR_COST_PER_RESTAURANT:,} MXN per visit')
restaurant_profit = MONTHLY_SUBSCRIPTION_FEE - CREATOR_COST_PER_RESTAURANT
print(f'Platform profit per restaurant: ${restaurant_profit:,} MXN/month')
print()

# Per Category Analysis (20 restaurants)
print('PER CATEGORY (20 restaurants, monthly):')
total_monthly_revenue = RESTAURANTS_PER_CATEGORY * MONTHLY_SUBSCRIPTION_FEE
total_monthly_creator_costs = RESTAURANTS_PER_CATEGORY * CREATOR_COST_PER_RESTAURANT
category_profit_no_marketing = total_monthly_revenue - total_monthly_creator_costs

print(f'Total monthly revenue: ${total_monthly_revenue:,} MXN')
print(f'Total monthly creator costs: ${total_monthly_creator_costs:,} MXN')
print(f'Platform profit per category (no marketing): ${category_profit_no_marketing:,} MXN/month')
print()

# With Fixed Marketing Budget Analysis
print('WITH FIXED $5,000 MXN MARKETING BUDGET:')
# Marketing budget is fixed per month, not per category
category_profit_with_fixed_marketing = total_monthly_revenue - total_monthly_creator_costs

print(f'Fixed marketing budget: ${FIXED_MARKETING_BUDGET:,} MXN per month')
print(f'Total monthly revenue: ${total_monthly_revenue:,} MXN')
print(f'Monthly creator costs: ${total_monthly_creator_costs:,} MXN')
print(f'Platform profit per category (before marketing): ${category_profit_with_fixed_marketing:,} MXN/month')
print()

# Monthly Revenue Scenarios
print('MONTHLY REVENUE SCENARIOS:')
scenarios = [1, 4, 10, 20, 50]

for categories in scenarios:
    restaurants = categories * RESTAURANTS_PER_CATEGORY
    monthly_revenue = restaurants * MONTHLY_SUBSCRIPTION_FEE
    monthly_creator_costs = restaurants * CREATOR_COST_PER_RESTAURANT
    # Marketing budget is fixed per month, not per category
    monthly_profit = monthly_revenue - monthly_creator_costs - FIXED_MARKETING_BUDGET
    print(f'{categories:2d} categories ({restaurants:4d} restaurants): ${monthly_revenue:8,.0f} MXN revenue, ${monthly_profit:8,.0f} MXN profit')

print()

# ROI Scenarios for Fixed Marketing Budget
print('MARKETING BUDGET ROI SCENARIOS:')
roi_scenarios = [2, 3, 5]

for roi in roi_scenarios:
    expected_new_revenue = FIXED_MARKETING_BUDGET * roi
    new_restaurants = expected_new_revenue / MONTHLY_SUBSCRIPTION_FEE
    print(f'ROI {roi}x: ${FIXED_MARKETING_BUDGET:,} MXN spend → ${expected_new_revenue:,} MXN revenue ({new_restaurants:.0f} new restaurants)')

print()

# Summary of Key Numbers
print('=== SUMMARY ===')
print(f'✅ Per restaurant profit: ${restaurant_profit:,} MXN/month')
print(f'✅ Per category profit (no marketing): ${category_profit_no_marketing:,} MXN/month')
print(f'✅ Per category profit (before marketing): ${category_profit_with_fixed_marketing:,} MXN/month')
print(f'✅ Fixed marketing budget: ${FIXED_MARKETING_BUDGET:,} MXN creates predictable costs')
print(f'✅ Monthly subscription model provides recurring revenue!')
print(f'✅ You are PROFITABLE from Month 1 with 4 categories!')
