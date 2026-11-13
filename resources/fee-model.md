# Delivery Order Fee Model

## All-in total
`items + tax + delivery + service + small-order + regulatory + other fees + tip - discounts - credits`

Use only fee categories actually shown by the checkout or receipt. Avoid double-counting a fee included in another line.

## Budget status
- Under budget: all-in total is less than or equal to the cap.
- Over budget: all-in total exceeds the cap.
- Unknown: one or more material charges are missing or unverified.

## Scenario comparison
Compare options using the same assumptions:
- same delivery address and time;
- same tip policy;
- same tax treatment;
- same discount eligibility;
- same fee inclusion.

A lower menu subtotal is not necessarily a lower final total. Recalculate after checkout updates.
