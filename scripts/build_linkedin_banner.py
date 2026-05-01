#!/usr/bin/env python3
"""Build LinkedIn company banner for Keys Touch — 1128x191 standard + 2256x382 retina."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path("/Users/keyscales/Documents/Key's Touch/Website")
SRC = ROOT / "images/social-banner.jpg"
OUT_DIR = ROOT / "brand-assets/social"
OUT_DIR.mkdir(parents=True, exist_ok=True)

INK = (15, 14, 12)
EMBER = (210, 125, 74)
IVORY = (246, 241, 231)

def font(size, bold=True):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def build(scale=2, profile=False):
    if profile:
        W, H = 1584 * scale, 396 * scale
    else:
        W, H = 1128 * scale, 191 * scale

    canvas = Image.new("RGB", (W, H), INK)

    src = Image.open(SRC).convert("RGB")
    src_ratio = src.width / src.height
    canvas_ratio = W / H
    # Cover-fit: scale source so it fills BOTH dimensions (no empty bars).
    if src_ratio > canvas_ratio:
        # Source wider than canvas — fit height, crop horizontal.
        target_h = H
        target_w = int(target_h * src_ratio)
    else:
        # Source taller than canvas — fit width, crop vertical.
        target_w = W
        target_h = int(target_w / src_ratio)
    src_resized = src.resize((target_w, target_h), Image.LANCZOS)
    crop_x = max(0, (target_w - W) // 2)
    crop_y = max(0, (target_h - H) // 2)
    src_cropped = src_resized.crop((crop_x, crop_y, crop_x + W, crop_y + H))
    canvas.paste(src_cropped, (0, 0))

    # Soft ink darken behind text band (left ~70%) — preserves wood texture, kills harsh black void.
    fade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fade)
    fade_w = int(W * (0.72 if not profile else 0.70))
    for x in range(fade_w):
        # max alpha 165 (down from 235) so the photo shows through
        alpha = int(165 * (1 - x / fade_w) ** 1.2)
        fd.line([(x, 0), (x, H)], fill=(*INK, alpha))

    canvas = Image.alpha_composite(canvas.convert("RGBA"), fade).convert("RGB")

    d = ImageDraw.Draw(canvas)

    if profile:
        # LinkedIn personal profile pic overlays bottom-left circle ~152px wide,
        # center at approx (130, H-72). Shift text right to clear it.
        pad_x = 260 * scale
        eyebrow_size = 22 * scale
        tag_size = 64 * scale
        sub_size = 22 * scale
    else:
        # Company page: clear logo overlay (right edge ~x=320) and brass key (left edge ~x=860).
        # Text fits in 540px-wide center band starting at pad_x=480.
        pad_x = 480 * scale
        eyebrow_size = 14 * scale
        tag_size = 32 * scale
        sub_size = 14 * scale

    eyebrow = font(eyebrow_size, bold=True)
    tag = font(tag_size, bold=True)
    sub = font(sub_size, bold=False)

    eyebrow_text = "AI AUTOMATION  ·  AI CONSULTING"
    tag_l1 = "We speak business."
    tag_l2 = "We build AI."
    sub_text = "TOUCH Framework  ·  Ship in 4 weeks  ·  Own your code"

    # Vertical block centered
    eb_bbox = d.textbbox((0, 0), eyebrow_text, font=eyebrow)
    t1_bbox = d.textbbox((0, 0), tag_l1, font=tag)
    t2_bbox = d.textbbox((0, 0), tag_l2, font=tag)
    sub_bbox = d.textbbox((0, 0), sub_text, font=sub)

    eb_h = eb_bbox[3] - eb_bbox[1]
    t1_h = t1_bbox[3] - t1_bbox[1]
    t2_h = t2_bbox[3] - t2_bbox[1]
    sub_h = sub_bbox[3] - sub_bbox[1]

    gap_eb = 10 * scale
    gap_tag = 4 * scale
    gap_sub = 12 * scale

    block_h = eb_h + gap_eb + t1_h + gap_tag + t2_h + gap_sub + sub_h
    if profile:
        # Bottom-align next to profile pic. Profile pic center sits ~y=H-72 visually.
        # Place block so it visually sits beside lower half of banner (where pic shows).
        y0 = H - block_h - (60 * scale)
    else:
        y0 = (H - block_h) // 2

    # Ember tick before eyebrow
    tick_w = 28 * scale
    tick_h = 3 * scale
    d.rectangle([pad_x, y0 + eb_h // 2 - tick_h // 2, pad_x + tick_w, y0 + eb_h // 2 + tick_h // 2], fill=EMBER)

    text_x = pad_x + tick_w + 14 * scale
    d.text((text_x, y0), eyebrow_text, font=eyebrow, fill=EMBER)

    y = y0 + eb_h + gap_eb
    d.text((pad_x, y), tag_l1, font=tag, fill=IVORY)
    y += t1_h + gap_tag
    d.text((pad_x, y), tag_l2, font=tag, fill=IVORY)
    y += t2_h + gap_sub
    d.text((pad_x, y), sub_text, font=sub, fill=(200, 195, 180))

    return canvas

# Render at 4x supersample then downsample to 2x retina for crisp text edges.
# Cache-bust filename with versioned suffix (LinkedIn caches uploads aggressively).
import time
v = time.strftime("%Y%m%d-%H%M")
oversample = build(scale=4)
retina = oversample.resize((2256, 382), Image.LANCZOS)
retina_path = OUT_DIR / f"linkedin-banner-v{v}.jpg"
retina.save(retina_path, "JPEG", quality=96, optimize=True, subsampling=0)
# Also keep canonical filename in sync
canonical = OUT_DIR / "linkedin-banner.jpg"
retina.save(canonical, "JPEG", quality=96, optimize=True, subsampling=0)

standard = retina.resize((1128, 191), Image.LANCZOS)
standard_path = OUT_DIR / "linkedin-banner-1x.jpg"
standard.save(standard_path, "JPEG", quality=96, optimize=True, subsampling=0)

# Personal profile variant (1584x396) — also supersampled
profile_oversample = build(scale=4, profile=True)
profile_retina = profile_oversample.resize((3168, 792), Image.LANCZOS)
profile_retina_path = OUT_DIR / "linkedin-profile-banner.jpg"
profile_retina.save(profile_retina_path, "JPEG", quality=96, optimize=True, subsampling=0)

profile_standard = profile_retina.resize((1584, 396), Image.LANCZOS)
profile_standard_path = OUT_DIR / "linkedin-profile-banner-1x.jpg"
profile_standard.save(profile_standard_path, "JPEG", quality=96, optimize=True, subsampling=0)

print(f"Wrote {retina_path} ({retina.size})")
print(f"Wrote {standard_path} ({standard.size})")
print(f"Wrote {profile_retina_path} ({profile_retina.size})")
print(f"Wrote {profile_standard_path} ({profile_standard.size})")
