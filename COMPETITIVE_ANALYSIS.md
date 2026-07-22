# Curefoods website rebuild — competitive analysis & AEO brief

## 1. Why this rebuild exists

An AEO audit of curefoods.in and five of its brand sites (2026-07-21) found the
corporate site in the worst shape of any Curefoods property:

| Check | curefoods.in (live, today) |
|---|---|
| Homepage HTML | ~2KB client-side redirect shell: `Loading... Redirecting to About Us...` — invisible to any non-JS crawler or AI bot |
| Title tag | Literally `"Loading..."` |
| robots.txt | Does not exist (404) |
| llms.txt | Does not exist (404) |
| sitemap.xml | Does not exist (404) |
| Structured data | None — can't evaluate, there's no server-rendered content to hold it |

Meanwhile the individual brand sites are a mixed bag — Sharief Bhai and Frozen
Bottle (Shopify) already have real menus, prices and agentic-commerce
infrastructure; Krispy Kreme India has zero JSON-LD anywhere and a broken
store-locator leaking a raw cURL SSL error into production HTML; Arambam has
no menu, no FAQ, and a duplicated/broken title tag (`"Arambam - arambam"`).

**The corporate site is the single highest-leverage fix**: it's the page any
answer engine (ChatGPT, Perplexity, Google AI Overviews) would reach for when
asked "what is Curefoods" or "what brands does Curefoods own" — and today it
hands them nothing to read.

## 2. Brands benchmarked against

Curefoods runs a **house-of-brands** model — several independently-branded
products on shared kitchen infrastructure. That structure has few close
analogs, so the benchmark set mixes direct structural peers with best-in-class
single-brand ordering UX:

| Brand | Why it's in the set |
|---|---|
| **Rebel Foods** (Faasos, Behrouz Biryani, Oven Story, Sweet Truth) | India's largest cloud-kitchen house-of-brands operator — the closest direct competitor to Curefoods, same category, same country, same shared-kitchen model. |
| **Americana Restaurants International** (KFC, Pizza Hut, Hardee's, Krispy Kreme, TGI Fridays across MENA) | A publicly-listed, multi-brand restaurant operator — the closest analog for how a *corporate/investor-facing* house-of-brands site should read, and notably also runs Krispy Kreme as a franchise, same as Curefoods. |
| **Yum! Brands** (KFC, Pizza Hut, Taco Bell) | The canonical global house-of-brands corporate site pattern — portfolio page separate from consumer ordering, strong investor/franchise section. |
| **Domino's** | Best-in-class single-brand ordering UX and PWA/app performance — the bar for "order flow," not portfolio structure. |
| **KFC** | Global QSR brand site conventions — nutrition/menu transparency, store locator patterns, loyalty integration. |

**Best patterns pulled from these into the rebuild:**
- Rebel Foods / Yum!: one hub page listing every brand as a first-class card, each linking to its own brand-specific micro-site rather than burying brands in a dropdown.
- Americana: clear separation of consumer content (brands, ordering) from corporate content (investors, newsroom, careers), with the corporate narrative (founder, funding, scale stats) given its own real estate instead of being an afterthought.
- Domino's/KFC: direct, above-the-fold ordering CTAs on every brand page — no brand page in this rebuild is more than one click from "order now."

## 3. Feature comparison matrix

| Capability | curefoods.in (before) | This rebuild | Rebel Foods | Americana | Yum! Brands | Domino's/KFC |
|---|---|---|---|---|---|---|
| Server-rendered homepage content | ❌ (JS redirect shell) | ✅ | ✅ | ✅ | ✅ | ✅ |
| robots.txt allowing AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | ❌ | ✅ | Partial | Partial | Partial | Partial |
| llms.txt | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Organization/Brand/FAQPage/BreadcrumbList JSON-LD | ❌ | ✅ (all pages) | Partial | Partial | Partial | ✅ (product schema) |
| Direct-answer boxes per brand (citable 1-sentence definitions) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Every brand as a first-class page (not just a logo strip) | ❌ | ✅ (15 brand pages) | Partial | ✅ | ✅ | n/a (single brand) |
| PWA (installable, offline fallback) | ❌ | ✅ | Partial | ❌ | ❌ | ✅ |
| Dark mode | ❌ | ✅ | ❌ | ❌ | ❌ | Partial |
| Disambiguation content for AI (e.g. "not the same as Rebel Foods") | ❌ | ✅ | n/a | n/a | n/a | n/a |
| Owned-brand vs. franchise-brand distinction stated explicitly | ❌ | ✅ (Krispy Kreme flagged as master-franchise, not owned IP) | n/a | ✅ | ✅ | n/a |

## 4. What was built

- **15 brand pages** (EatFit, Sharief Bhai, Roz Shawarma, Nomad Pizza, Frozen Bottle, Olio, CakeZone, Rolls on Wheels, Great Indian Khichdi, Homeplate, Chaat Street, Millet Express, Madras Curd Rice Company, Arambam, Krispy Kreme) — each with story, menu highlights, cities served, FAQ, and direct order links.
- **Real order routing**: brands with confirmed live D2C domains (Sharief Bhai → shariefbhai.com, Frozen Bottle → frozenbottle.com, Olio → oliopizza.in, Krispy Kreme → krispykremeindia.in, Arambam → arambam.com) link straight to their own site as the primary CTA; every brand also gets Swiggy/Zomato search-deeplink fallbacks.
- **Full AEO stack**: robots.txt (explicit AI-crawler allowlist), llms.txt (facts + brand index + AI-assistant disambiguation notes), sitemap.xml, JSON-LD `@graph` (Organization, WebSite, Brand, FAQPage, BreadcrumbList, ItemList, AboutPage, ContactPage) on every page.
- **PWA**: manifest.json, service worker with offline fallback page, installable on mobile home screens.
- **Design system**: Fraunces/Inter type pairing, light/dark theme (system + manual toggle), mobile-first responsive grid, accessible focus states, reduced-motion support.
- **Content engine**: `build/data.py` + `build/generate.py` — a static-site generator, so editing brand copy/menus/FAQs is a data-file edit + one command (`python3 build/generate.py`), not hand-editing 27 HTML files.

## 5. Known gaps before a real production launch

- **Imagery**: brand marks are placeholder color-block SVGs, not real logos/photography — swap in real brand assets before launch.
- **Menu data**: menu highlights and prices are illustrative, not pulled from a live menu/pricing system — needs a real feed before "10x better" claims extend to accuracy.
- **Deep links**: Swiggy/Zomato links use generic search URLs, not verified per-brand, per-city storefront IDs.
- **Legal pages**: privacy policy and terms are explicit placeholders pending legal review.
- **Analytics/consent**: no analytics or cookie-consent layer wired in yet.
- **Stats**: FY24 revenue, kitchen count, and city count are sourced from public reporting and should be reconciled against internal finance numbers before publishing.
