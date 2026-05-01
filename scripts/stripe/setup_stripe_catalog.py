#!/usr/bin/env python3
"""Idempotent Stripe catalog setup for Key's Touch.

Creates 6 products + 13 prices via Stripe API. Safe to re-run — uses
lookup_keys on prices and matches products by metadata key, so duplicates
are avoided.

Usage:
    pip install stripe
    export STRIPE_API_KEY=sk_test_...   # use test key first!
    python3 setup_stripe_catalog.py --dry-run
    python3 setup_stripe_catalog.py     # actually create
    python3 setup_stripe_catalog.py --live  # require sk_live_ key

Outputs JSON map of {product_name: {id, prices: {nickname: price_id}}}
to ./stripe-catalog.json so you can reference IDs later.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import stripe
except ImportError:
    print("ERROR: pip install stripe", file=sys.stderr)
    sys.exit(1)

CATALOG = [
    {
        "key": "ai_agent_development",
        "name": "AI Agent Development",
        "description": "24/7 autonomous AI agents for customer service, lead qualification, data processing, and operations.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",  # SaaS - business use
        "prices": [],  # custom-quoted per engagement
    },
    {
        "key": "ai_automation_workflows",
        "name": "AI Automation & Workflows",
        "description": "End-to-end automation of repetitive operations using LLMs, integrations, and rule-based workflows.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [],
    },
    {
        "key": "saas_product_development",
        "name": "SaaS Product Development",
        "description": "Idea to MVP shipped in 6-10 weeks. Full source code ownership, no vendor lock-in.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [],
    },
    {
        "key": "custom_software_development",
        "name": "Custom Software Development",
        "description": "Bespoke web apps, internal tools, and integrations engineered for ownership and longevity.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [],
    },
    {
        "key": "website_development",
        "name": "Website Development",
        "description": "High-performance, SEO-optimized, brand-aligned websites and web apps.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [
            {"lookup_key": "kt_brand_spark",       "nickname": "Brand Spark",                          "amount_usd": 4500,  "type": "one_time"},
            {"lookup_key": "kt_brand_web",         "nickname": "Brand + Web",                          "amount_usd": 11000, "type": "one_time"},
            {"lookup_key": "kt_brand_web_setup",   "nickname": "Brand + Web + Ongoing - Setup",        "amount_usd": 14000, "type": "one_time"},
            {"lookup_key": "kt_retainer_monthly",  "nickname": "Brand + Web + Ongoing - Retainer",     "amount_usd": 2500,  "type": "recurring", "interval": "month"},
        ],
    },
    {
        "key": "ai_automation_consulting",
        "name": "AI & Automation Consulting",
        "description": "Strategy, governance, team upskilling. Free 30-min audit available.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [
            {"lookup_key": "kt_free_audit",         "nickname": "Free Audit (30-min)",   "amount_usd": 0,    "type": "one_time"},
            {"lookup_key": "kt_strategy_fee",       "nickname": "Strategy Fee",          "amount_usd": 500,  "type": "one_time"},
            {"lookup_key": "kt_consulting_day",     "nickname": "Consulting Day Rate",   "amount_usd": 2500, "type": "one_time"},
            {"lookup_key": "kt_governance_retainer","nickname": "Governance Retainer",   "amount_usd": 5000, "type": "recurring", "interval": "month"},
        ],
    },
    {
        "key": "addons",
        "name": "Add-ons",
        "description": "A la carte add-ons available alongside any Key's Touch engagement.",
        "statement_descriptor": "KEYSTOUCH",
        "tax_code": "txcd_10103001",
        "prices": [
            {"lookup_key": "kt_addon_pitch_deck",        "nickname": "Pitch deck template",      "amount_usd": 1200, "type": "one_time"},
            {"lookup_key": "kt_addon_email_signature",   "nickname": "Email signature templates","amount_usd": 400,  "type": "one_time"},
            {"lookup_key": "kt_addon_notion_workspace",  "nickname": "Notion brand workspace",   "amount_usd": 800,  "type": "one_time"},
            {"lookup_key": "kt_addon_logo_redraw",       "nickname": "Custom vector logo redraw","amount_usd": 2250, "type": "one_time"},
        ],
    },
]


def find_or_create_product(key: str, spec: dict, dry: bool) -> stripe.Product:
    """Idempotent: match by metadata.kt_key. Create if missing."""
    existing = stripe.Product.search(query=f'metadata["kt_key"]:"{key}" AND active:"true"', limit=1)
    if existing.data:
        prod = existing.data[0]
        print(f"  [exists] product: {spec['name']} ({prod.id})")
        return prod
    if dry:
        print(f"  [DRY-RUN] would create product: {spec['name']}")
        return None
    prod = stripe.Product.create(
        name=spec["name"],
        description=spec["description"],
        statement_descriptor=spec["statement_descriptor"],
        tax_code=spec["tax_code"],
        metadata={"kt_key": key},
    )
    print(f"  [created] product: {spec['name']} ({prod.id})")
    return prod


def find_or_create_price(product: stripe.Product, price_spec: dict, dry: bool) -> stripe.Price:
    """Idempotent: lookup_key is unique. Update if found with mismatch is NOT allowed —
    Stripe prices are immutable once created. Skip with warning if amount mismatches."""
    lookup_key = price_spec["lookup_key"]
    existing = stripe.Price.list(lookup_keys=[lookup_key], active=True, limit=1)
    target_amount = price_spec["amount_usd"] * 100  # cents
    if existing.data:
        p = existing.data[0]
        if p.unit_amount != target_amount:
            print(f"    [WARNING] price {lookup_key} exists at ${p.unit_amount/100} but spec says ${price_spec['amount_usd']}. Stripe prices are immutable — archive old + create new manually.")
        else:
            print(f"    [exists] price: {price_spec['nickname']} ({p.id})")
        return p
    if dry:
        print(f"    [DRY-RUN] would create price: {price_spec['nickname']} ${price_spec['amount_usd']} ({price_spec['type']})")
        return None
    args = {
        "currency": "usd",
        "unit_amount": target_amount,
        "lookup_key": lookup_key,
        "nickname": price_spec["nickname"],
        "product": product.id,
        "tax_behavior": "exclusive",
    }
    if price_spec["type"] == "recurring":
        args["recurring"] = {"interval": price_spec.get("interval", "month")}
    p = stripe.Price.create(**args)
    print(f"    [created] price: {price_spec['nickname']} ({p.id})")
    return p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview only — no API writes")
    parser.add_argument("--live", action="store_true", help="Require sk_live_ key (safety check)")
    parser.add_argument("--api-key", help="Override STRIPE_API_KEY env var")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("STRIPE_API_KEY")
    if not api_key:
        print("ERROR: set STRIPE_API_KEY env var or pass --api-key", file=sys.stderr)
        sys.exit(1)

    if args.live and not api_key.startswith("sk_live_"):
        print("ERROR: --live requires a sk_live_ key", file=sys.stderr)
        sys.exit(1)
    if not args.live and api_key.startswith("sk_live_"):
        print("ERROR: live key detected without --live flag. Add --live to confirm.", file=sys.stderr)
        sys.exit(1)

    stripe.api_key = api_key
    mode = "LIVE" if api_key.startswith("sk_live_") else "TEST"
    print(f"\nStripe mode: {mode}")
    print(f"Dry run: {args.dry_run}\n")

    catalog_out = {}
    for spec in CATALOG:
        print(f"\n{spec['name']}")
        product = find_or_create_product(spec["key"], spec, args.dry_run)
        prices = {}
        for price_spec in spec["prices"]:
            price = find_or_create_price(product, price_spec, args.dry_run) if product else None
            if price:
                prices[price_spec["nickname"]] = price.id
        catalog_out[spec["name"]] = {
            "id": product.id if product else None,
            "key": spec["key"],
            "prices": prices,
        }

    if not args.dry_run:
        out_path = Path(__file__).parent / f"stripe-catalog-{mode.lower()}.json"
        out_path.write_text(json.dumps(catalog_out, indent=2))
        print(f"\nWrote catalog map to {out_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
