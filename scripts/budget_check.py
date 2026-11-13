#!/usr/bin/env python3
"""Calculate an all-in order total against a user-defined budget."""
import argparse
from decimal import Decimal, InvalidOperation

def dec(value):
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"Invalid decimal amount: {value}") from exc

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--budget", required=True, type=dec)
    p.add_argument("--items", default=Decimal("0"), type=dec)
    p.add_argument("--tax", default=Decimal("0"), type=dec)
    p.add_argument("--delivery", default=Decimal("0"), type=dec)
    p.add_argument("--service", default=Decimal("0"), type=dec)
    p.add_argument("--other-fees", default=Decimal("0"), type=dec)
    p.add_argument("--tip", default=Decimal("0"), type=dec)
    p.add_argument("--discounts", default=Decimal("0"), type=dec)
    args = p.parse_args()
    total = args.items + args.tax + args.delivery + args.service + args.other_fees + args.tip - args.discounts
    delta = args.budget - total
    print(f"All-in total: {total:.2f}")
    print(f"Budget:       {args.budget:.2f}")
    print(f"Remaining:    {delta:.2f}" if delta >= 0 else f"Over budget:  {-delta:.2f}")
    print("Status: UNDER BUDGET" if delta >= 0 else "Status: OVER BUDGET")

if __name__ == "__main__":
    main()
