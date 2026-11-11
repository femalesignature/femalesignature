#!/usr/bin/env python3
"""Bildplätze der Startseite.

    python3 tools/images.py

Für jeden Platz in SLOTS: liegt ein Original in images/src/<name>.(jpg|jpeg|png|webp),
wird es zugeschnitten und als WebP in allen Breiten nach images/opt/ geschrieben.
Fehlt es, entsteht ein Platzhalter im Markenstil. Danach build-home.py laufen lassen.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "images" / "src"
OUT = ROOT / "images" / "opt"

# name: (Seitenverhältnis B/H, Breiten, Platzhalter-Beschriftung)
SLOTS = {
    "s1-brand":       (4 / 3, (600, 900, 1200), "01 Brand Experience"),
    "s2-content":     (4 / 3, (600, 900, 1200), "02 Content & Sichtbarkeit"),
    "s3-partnership": (4 / 3, (600, 900, 1200), "03 Partnership Marketing"),
    "s4-performance": (4 / 3, (600, 900, 1200), "04 Performance Marketing"),
    "approach":       (4 / 5, (480, 720, 960), "05 Ansatz / Workshop"),
    "about":          (4 / 5, (480, 720, 960), "06 Mediha (Shooting)"),
    "blog-1":         (4 / 3, (480, 720, 960), "07 Blog Partnerprogramme"),
    "blog-2":         (4 / 3, (480, 720, 960), "08 Blog Social Media"),
    "blog-3":         (4 / 3, (480, 720, 960), "09 Blog Female Empowerment"),
    "blog-4":         (4 / 3, (480, 720, 960), "11 Blog Partnership Marketing"),
    "blog-5":         (4 / 3, (480, 720, 960), "12 Blog Affiliate Marketing"),
    "blog-6":         (4 / 3, (480, 720, 960), "13 Blog Performance Marketing"),
    "blog-7":         (4 / 3, (480, 720, 960), "14 Blog Personal Branding"),
    "cta":            (21 / 9, (800, 1400, 2000), "10 Abschluss"),
}
# Breite Titelbilder der Blogartikel: gleiches Original wie die Karte, nur anders zugeschnitten
for _n in range(1, 8):
    SLOTS[f"cover-{_n}"] = (16 / 9, (800, 1200, 1600), f"Blog {_n} Titelbild")
SOURCE = {f"cover-{_n}": f"blog-{_n}" for _n in range(1, 8)}


# Ausschnitt-Mitte je Platz (x, y von 0 bis 1); Standard etwas über der Mitte
CENTER = {"about": (0.5, 0.0), "cta": (0.5, 0.6)}
# Plätze, bei denen oben Luft fehlt: so viel Hintergrund wird oben ergänzt (Anteil der Höhe)
HEADROOM = {"about": 0.06}

# Runde Porträts (Ausschnitt-Box im Original: links, oben, rechts, unten)
FACES = {
    "valeriya": ("valeriya.jpeg", (234, 170, 554, 490)),
    "mediha-face": ("src/about.jpg", (245, 40, 515, 310)),
}


def add_headroom(im, share):
    pad = round(im.height * share)
    top = im.crop((0, 0, im.width, 4)).resize((im.width, pad), Image.BILINEAR).filter(ImageFilter.GaussianBlur(6))
    out = Image.new("RGB", (im.width, im.height + pad))
    out.paste(top, (0, 0))
    out.paste(im, (0, pad))
    return out


def cover(im, ratio, w, center=(0.5, 0.35)):
    h = round(w / ratio)
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=center)


def placeholder(ratio, label):
    w = 1600 if ratio > 1 else 1200  # Platzhalter immer groß genug für die breiteste Datei
    h = round(w / ratio)
    im = Image.new("RGB", (w, h))
    top, bot = (233, 226, 215), (92, 31, 43)
    px = im.load()
    for y in range(h):
        t = (y / h) ** 1.6
        c = tuple(round(top[i] + (bot[i] - top[i]) * t * 0.55) for i in range(3))
        for x in range(w):
            px[x, y] = c
    noise = Image.effect_noise((w, h), 18).convert("L").filter(ImageFilter.GaussianBlur(0.6))
    im = Image.blend(im, Image.merge("RGB", (noise,) * 3), 0.05)
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", max(22, w // 34))
    except OSError:
        font = ImageFont.load_default()
    text = "PLATZHALTER  ·  " + label.upper()
    tw = d.textlength(text, font=font)
    d.text(((w - tw) / 2, h / 2 - font.size / 2), text, fill=(244, 241, 235), font=font)
    return im


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (ratio, widths, label) in SLOTS.items():
        base = SOURCE.get(name, name)
        src = next((p for ext in ("jpg", "jpeg", "png", "webp") for p in [SRC / f"{base}.{ext}"] if p.exists()), None)
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB") if src else placeholder(ratio, label)
        if src and name in HEADROOM:
            im = add_headroom(im, HEADROOM[name])
        for w in widths:
            out = OUT / f"{name}-{w}.webp"
            img = cover(im, ratio, min(w, im.width), CENTER.get(name, (0.5, 0.35)))
            for q in (72, 66, 60, 54, 48):  # Regel: jede Datei unter 100 KB
                img.save(out, quality=q, method=6)
                if out.stat().st_size < 100 * 1024:
                    break
        print(f"{name:15} {'ORIGINAL ' + src.name if src else 'Platzhalter'}  {max((OUT / f'{name}-{w}.webp').stat().st_size for w in widths) // 1024} KB max")
    for name, (rel, box) in FACES.items():
        f = ROOT / "images" / rel
        if not f.exists():
            continue
        im = ImageOps.exif_transpose(Image.open(f)).convert("RGB").crop(box)
        for w in (96, 192):
            im.resize((w, w), Image.LANCZOS).save(OUT / f"{name}-{w}.webp", quality=80, method=6)
        print(f"{name:15} Porträt 96/192")


if __name__ == "__main__":
    main()
