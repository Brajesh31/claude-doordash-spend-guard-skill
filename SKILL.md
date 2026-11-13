---
name: doordash-spend-guard
description: Helps users set order budgets, understand fees, compare scenarios, and avoid exceeding a chosen delivery-spend limit.
---

# DoorDash Spend Guard

Use this skill to help a user make a delivery-order decision within a stated budget.

## Workflow
1. Confirm the budget cap, currency, time period, and whether tip and fees count toward the cap.
2. Capture item subtotal, tax, delivery fee, service fee, small-order fee, tip, discounts, credits, and other displayed charges.
3. Distinguish current checkout values from estimates and historical averages.
4. Calculate the all-in total and remaining budget.
5. Compare lower-cost alternatives without changing the user's order.
6. Present a stop/go recommendation and the assumptions behind it.

## Rules
- Never hide fees or treat a pre-fee subtotal as the final total.
- Do not assume a promotion applies until visible at checkout.
- Do not pressure the user to spend more to unlock a discount.
- Do not claim access to account-wide spending unless the user supplies the records.
- Keep financial advice limited to budgeting arithmetic, not credit or debt advice.

## Output
Use `templates/order-budget.md` for planning and `resources/fee-model.md` for calculations. Show total, cap, remaining amount, and any unconfirmed charges.
