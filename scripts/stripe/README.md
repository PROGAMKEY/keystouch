# Stripe Catalog Automation — Key's Touch

Two paths to manage Stripe without clicking through the dashboard:

## Option A — One-shot Python script (fastest)

Run once. Creates 6 products + 13 prices in your Stripe account. Idempotent
(safe to re-run).

### Setup

```bash
pip install stripe
```

### Get your API key

1. Open https://dashboard.stripe.com/test/apikeys
2. Copy the **Secret key** (starts with `sk_test_...`) — TEST mode first
3. Export it:

```bash
export STRIPE_API_KEY=sk_test_xxxxxxxxxxxxx
```

### Dry run first (no writes)

```bash
cd ~/Documents/Key\'s\ Touch/Website/scripts/stripe
python3 setup_stripe_catalog.py --dry-run
```

Review output — should list 6 products + 13 prices it would create.

### Run for real (test mode)

```bash
python3 setup_stripe_catalog.py
```

Verify in Stripe Dashboard (top-right toggle on TEST). Confirm products + prices look correct.

### Switch to live mode

```bash
export STRIPE_API_KEY=sk_live_xxxxxxxxxxxxx
python3 setup_stripe_catalog.py --live
```

The `--live` flag is required when using a `sk_live_` key — extra safety check.

### Output

After a real (non-dry) run, a `stripe-catalog-{test,live}.json` file is written
with the product + price IDs. Use these IDs when scripting invoices later.

### Re-running

Safe. Products are matched by `metadata.kt_key`, prices by `lookup_key`. Existing
items are detected and skipped. To change a price amount, you must:
1. Archive the old price in Stripe Dashboard (prices are immutable in Stripe)
2. Update `amount_usd` in `setup_stripe_catalog.py`
3. Re-run — script will create the new price with the same `lookup_key`

---

## Option B — Stripe MCP server (ongoing conversational)

Lets you talk to Stripe directly from Claude/CLI without scripts. Best for
ongoing operations: create invoices, update customers, refund payments, etc.

### Install (Claude Desktop)

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "stripe": {
      "command": "npx",
      "args": ["-y", "@stripe/mcp", "--tools=all", "--api-key=sk_test_xxxxxxxxxxxxx"]
    }
  }
}
```

Replace `sk_test_xxxxxxxxxxxxx` with your test key. Restart Claude Desktop.

### Install (Claude Code CLI)

```bash
claude mcp add stripe \
  -- npx -y @stripe/mcp --tools=all --api-key=sk_test_xxxxxxxxxxxxx
```

### What MCP unlocks

After install, you can say things like:
- "Create a customer in Stripe for Acme Corp, billing email cfo@acme.com"
- "Send an invoice to Acme for the Brand + Web package, milestone 1, due net 14"
- "List the last 10 paid invoices and their amounts"
- "Refund invoice INV-2026-0042 in full"
- "Add a $1,200 line item for Pitch Deck Template to invoice INV-2026-0050"

No clicking through dashboards. Conversational ops.

### Tools available

`@stripe/mcp` exposes these scopes (set via `--tools=`):
- `customers.read,customers.write`
- `products.read,products.write`
- `prices.read,prices.write`
- `invoices.read,invoices.write`
- `paymentLinks.read,paymentLinks.write`
- `refunds.read,refunds.write`
- `subscriptions.read,subscriptions.write`
- `coupons.read,coupons.write`

`--tools=all` enables everything. Lock down to specific scopes once you know
what you need.

---

## Recommended order

1. **Now:** Run Option A in TEST mode (`sk_test_...`) — verifies pricing matches
   `pricing-packages.md` and gives you a clean catalog
2. **Verify:** Open Stripe Dashboard (TEST mode) → Products → confirm all 6 + 13
3. **Switch:** Re-run with `sk_live_...` + `--live` flag to populate live account
4. **Install Option B** for daily invoice + customer operations

After both: you have a fully populated Stripe + a conversational interface for
ongoing client billing. No more dashboard clicks.

---

## Troubleshooting

- **"No module named 'stripe'"** → `pip install stripe` (or `pip3`)
- **"Authentication required"** → wrong API key or expired
- **"Tax code invalid"** → SaaS tax code may have changed; remove `tax_code` line
  in `setup_stripe_catalog.py` if it errors (script has `txcd_10103001`)
- **Price already exists at different amount** → Stripe prices are immutable.
  Archive in Dashboard, update script, re-run.

---

## Related

- Pricing source-of-truth: `~/Documents/2026/Client Intake Materials/pricing-packages.md`
- Setup walkthrough: `~/Documents/2026/Keys Touch/Operations/Stripe Setup — Services + Invoicing.md`
- Stripe MCP repo: https://github.com/stripe/agent-toolkit
