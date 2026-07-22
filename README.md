# Curefoods — House of Brands (rebuild)

A from-scratch, AEO-optimized rebuild of curefoods.in — a static site covering
the corporate "house of brands" story plus a dedicated page per brand
(EatFit, Sharief Bhai, Roz Shawarma, Nomad Pizza, Frozen Bottle, Olio,
CakeZone, Krispy Kreme, Arambam, and the rest of the Kitchens-of-EatFit
family).

See [`COMPETITIVE_ANALYSIS.md`](./COMPETITIVE_ANALYSIS.md) for what's broken
on the live site today, which brands this was benchmarked against, and what's
still a placeholder.

## Editing content

All copy — brand list, taglines, menus, FAQs, stats, timeline — lives in
[`build/data.py`](./build/data.py). Nothing else needs to change for a
content edit.

```bash
python3 build/generate.py
```

This regenerates every HTML page, `sitemap.xml`, `robots.txt`, `llms.txt` and
`manifest.json` at the repo root from that one data file. No build tooling,
no npm install — GitHub Pages serves the generated files directly.

## Previewing locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Structure

```
build/data.py        content (edit this)
build/generate.py     generator (edit only for layout/schema changes)
assets/css/style.css  design system
assets/js/main.js     nav, theme toggle, FAQ, service-worker registration
brands/*.html         generated — one page per brand
*.html                generated — homepage, about, faq, careers, investors, ...
robots.txt, llms.txt, sitemap.xml, manifest.json, sw.js   generated — AEO + PWA
```

## What "AEO-friendly" means here

- Every page is server-rendered HTML (no client-side-only content) with a
  short direct-answer paragraph an AI assistant can quote directly.
- `robots.txt` explicitly allows GPTBot, ChatGPT-User, PerplexityBot,
  Google-Extended, ClaudeBot and Applebot-Extended.
- `llms.txt` lists every brand, key pages, and disambiguation notes (e.g.
  Curefoods ≠ Rebel Foods; Krispy Kreme is a franchise partner, not owned IP).
- JSON-LD (`Organization`, `Brand`, `FAQPage`, `BreadcrumbList`, `WebSite`,
  `ItemList`) on every relevant page.

## Status

Prototype for review/iteration — not yet pointed at the real curefoods.in
domain. See "Known gaps" in `COMPETITIVE_ANALYSIS.md` before production launch.
