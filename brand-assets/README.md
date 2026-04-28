# Key's Touch — Brand Assets (v1)

Brand: **Ink + Ember** palette · type: **Inter Tight + Inter** · locked 2026-04-28.

All assets here are downloadable for use on websites, social media, email
signatures, decks, and partner co-marketing.

## Folder map

```
brand-assets/
├── logo-mark/                 ← the K-mark only (square, no wordmark)
│   ├── transparent/{256,512,1024,2048}.png
│   ├── on-ink/{256,512,1024,2048}.png
│   ├── on-ivory/{256,512,1024,2048}.png
│   └── key-mark.svg            ← scales infinitely (raster-embedded)
├── wordmark/                  ← "Key's Touch" type-only
│   ├── keys-touch.svg          ← ink (default)
│   ├── keys-touch-ivory.svg
│   ├── keys-touch-ember.svg
│   └── keys-touch-{on-ivory,on-ink,ember-on-ink}.png
└── combo-lockup/              ← mark + wordmark, side-by-side
    ├── lockup-on-ivory-{256,512,1024,2048}.png
    ├── lockup-on-ink-{256,512,1024,2048}.png
    ├── lockup-on-ivory.svg
    └── lockup-on-ink.svg
```

## Quick picks for common platforms

| Platform | File |
|---|---|
| LinkedIn profile photo (400×400) | `logo-mark/on-ink/512.png` (cropped square) |
| LinkedIn company logo (300×300) | `logo-mark/transparent/512.png` |
| LinkedIn cover banner (1584×396) | use `social-banner.jpg` from /images/ — see brand-book § photography |
| X/Twitter avatar (400×400) | `logo-mark/on-ink/512.png` |
| Instagram profile (320×320) | `logo-mark/transparent/512.png` |
| Facebook page (180×180) | `logo-mark/transparent/512.png` |
| Email signature (max 120×120) | `logo-mark/transparent/256.png` |
| Slack workspace icon (132×132) | `logo-mark/transparent/256.png` |
| Favicon (already deployed) | `/images/favicon.ico` |
| Apple touch icon (already deployed) | `/images/apple-touch-icon.png` |
| GitHub org/profile (1000×1000) | `logo-mark/on-ink/1024.png` |
| Print (≥300dpi business card) | `combo-lockup/lockup-on-ivory-2048.png` |

## Direct download URLs (after deploy)

Replace `keystouch.com` with whatever your live host is.

```
https://keystouch.com/brand-assets/logo-mark/transparent/512.png
https://keystouch.com/brand-assets/logo-mark/on-ink/1024.png
https://keystouch.com/brand-assets/wordmark/keys-touch.svg
https://keystouch.com/brand-assets/combo-lockup/lockup-on-ivory-1024.png
```

## Usage rules

See full guidelines in `~/Documents/2026/Keys Touch/Brand Guidelines/brand-book.md`.

Quick rules:
- **Never** stretch, recolor, or add effects (drop shadow, glow, gradient overlay)
- **Never** put the mark on a busy photo without an ink/ivory padding pad
- **Always** preserve the apostrophe in "Key's Touch"
- **Always** leave clear space ≥ 1× the height of the mark on every side
- Minimum size: **24px wide** for the mark, **120px wide** for the wordmark

## Future replacements (queued)

- The current K-mark is a recolored version of the previous cyan logo. A
  proper vector redraw is queued in brand-book.md § 10. When that lands,
  this folder will be regenerated and old files retained at
  `/brand-assets/_archive-v1/` for reference.
- Söhne typeface license (replaces Inter Tight) — when revenue justifies.
