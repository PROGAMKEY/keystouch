#!/usr/bin/env python3
"""Recolor the logo from #F06020 (old saturated orange) to brand ember #D27D4A.

Per-pixel HSL shift on orange-family pixels only — leaves whites + transparent alone.
"""
from PIL import Image
import colorsys
from pathlib import Path

SRC = Path("/Users/keyscales/Downloads/key touch logo icon (1).png")  # 4000x4000 master
OUT_DIR = Path("/Users/keyscales/Documents/Key's Touch/Website/brand-assets/social")
LOGO_MARK_DIR = Path("/Users/keyscales/Documents/Key's Touch/Website/brand-assets/logo-mark/transparent")

# Brand ember target (HSL): hue=21°, sat=58%, lightness=56%
EMBER_H = 21 / 360
EMBER_S = 0.58

def recolor(im):
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 10:
                continue
            r1, g1, b1 = r / 255, g / 255, b / 255
            hh, ll, ss = colorsys.rgb_to_hls(r1, g1, b1)
            # Recolor any saturated chromatic pixel (blue, orange, etc.) to ember.
            # Skip whites/grays (low saturation).
            if ss > 0.20:
                new_s = min(max(ss, 0.45), EMBER_S)
                new_l = ll * 0.85 + 0.05
                nr, ng, nb = colorsys.hls_to_rgb(EMBER_H, new_l, new_s)
                px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255), a)
    return im

def main():
    src_img = Image.open(SRC)
    print(f"Loading source: {SRC} ({src_img.size})")

    # First check: source might be cyan original. Recolor needs to handle cyan->ember too.
    # Sample dominant non-white opaque color to detect.
    sample = src_img.convert("RGBA").resize((100, 100), Image.LANCZOS)
    from collections import Counter
    c = Counter()
    for px_x in range(0, 100, 2):
        for px_y in range(0, 100, 2):
            r, g, b, a = sample.getpixel((px_x, px_y))
            if a > 200 and not (r > 240 and g > 240 and b > 240):
                c[(r // 16, g // 16, b // 16)] += 1
    if c:
        top = c.most_common(1)[0][0]
        tr, tg, tb = top[0] * 16, top[1] * 16, top[2] * 16
        print(f"Source dominant: RGB({tr},{tg},{tb})")

    recolored = recolor(src_img)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOGO_MARK_DIR.mkdir(parents=True, exist_ok=True)

    # LinkedIn-ready sizes
    for size in [400, 1024, 2048]:
        out_path = OUT_DIR / f"linkedin-logo-{size}.png"
        resized = recolored.resize((size, size), Image.LANCZOS)
        resized.save(out_path, "PNG", optimize=True)
        print(f"Wrote {out_path}")

    # Brand-assets master (overwrite the saturated one)
    for size in [256, 512, 1024, 2048]:
        out_path = LOGO_MARK_DIR / f"{size}.png"
        resized = recolored.resize((size, size), Image.LANCZOS)
        resized.save(out_path, "PNG", optimize=True)
        print(f"Wrote {out_path}")

    # On-ink JPEG for platforms that reject transparent PNGs
    on_ink = recolored.resize((1024, 1024), Image.LANCZOS)
    bg = Image.new("RGB", on_ink.size, (15, 14, 12))
    bg.paste(on_ink, mask=on_ink.split()[3])
    bg.save(OUT_DIR / "linkedin-logo-1024-on-ink.jpg", "JPEG", quality=96, optimize=True, subsampling=0)
    print(f"Wrote {OUT_DIR}/linkedin-logo-1024-on-ink.jpg")

if __name__ == "__main__":
    main()
