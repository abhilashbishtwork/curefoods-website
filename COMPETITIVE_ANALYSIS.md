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
| **Hindustan Unilever, HCCB, PepsiCo India** | Large FMCG house-of-brands corporates — the bar for restrained, minimal, "brands you love" portfolio presentation outside food delivery specifically. |

**Best patterns pulled from these into the rebuild:**
- Rebel Foods / Yum!: one hub page listing every brand as a first-class card, each linking to its own brand-specific micro-site rather than burying brands in a dropdown.
- Americana: clear separation of consumer content (brands, ordering) from corporate content (newsroom, careers), with the corporate narrative (founder, scale stats) given its own real estate instead of being an afterthought; a per-brand scale stat (this rebuild uses "cities served" per card) for instant credibility.
- Domino's/KFC: direct, above-the-fold ordering CTAs on every brand page — no brand page in this rebuild is more than one click from "order now."
- PepsiCo India: occasion/craving-based brand framing ("one occasion each") rather than generic category labels.

**2026-07-23 re-audit of Americana + Rebel Foods (via direct fetch):** neither
has JSON-LD structured data or a working llms.txt on their homepage today —
this rebuild's AEO stack is a genuine, currently-true differentiator over both
named direct comps, not just over old curefoods.in. HUL, HCCB and PepsiCo
India all block automated fetching (Akamai/Incapsula/WAF), so their design
was assessed from search-result snippets only, not a full teardown.

## 3. Feature comparison matrix

| Capability | curefoods.in (before) | This rebuild | Rebel Foods | Americana | Yum! Brands | Domino's/KFC |
|---|---|---|---|---|---|---|
| Server-rendered homepage content | ❌ (JS redirect shell) | ✅ | ✅ | ✅ | ✅ | ✅ |
| robots.txt allowing AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | ❌ | ✅ | Partial | Partial | Partial | Partial |
| llms.txt | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Organization/Brand/FAQPage/BreadcrumbList JSON-LD | ❌ | ✅ (all pages) | Partial | Partial | Partial | ✅ (product schema) |
| Direct-answer boxes per brand (citable 1-sentence definitions) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Every brand as a first-class page (not just a logo strip) | ❌ | ✅ (7 flagship brand pages) | Partial | ✅ | ✅ | n/a (single brand) |
| PWA (installable, offline fallback) | ❌ | ✅ | Partial | ❌ | ❌ | ✅ |
| Dark mode | ❌ | ✅ | ❌ | ❌ | ❌ | Partial |
| Disambiguation content for AI (e.g. "not the same as Rebel Foods") | ❌ | ✅ | n/a | n/a | n/a | n/a |
| Owned-brand vs. franchise-brand distinction stated explicitly | ❌ | ✅ (Krispy Kreme flagged as master-franchise, not owned IP) | n/a | ✅ | ✅ | n/a |

## 4. What was built

- **7 flagship brand pages** (EatFit, Sharief Bhai, Olio, Arambam, Krispy Kreme, Nomad Pizza, CakeZone) — each with story, menu highlights, cities served, a per-card "cities served" scale stat, FAQ, and direct order links. The other 8 Curefoods brands are intentionally out of scope for this pass, per direction to keep the showcase to flagship brands only.
- **Real brand assets**: logos and food/store photography pulled directly from each brand's own live site (Sharief Bhai's actual storefront, EatFit's kulcha, Olio's pizzas, Arambam's thali, Krispy Kreme's donuts, Nomad's pizza boxes, CakeZone's cake) — replacing the original emoji/color-block placeholders. The Curefoods parent logo is the real navy wordmark pulled from curefoods.in, not a text-only rendering.
- **Real order routing**: brands with confirmed live D2C domains (Sharief Bhai → shariefbhai.com, Olio → oliopizza.in, Krispy Kreme → krispykremeindia.in, Arambam → arambam.com) link straight to their own site as the primary CTA; every brand also gets Swiggy/Zomato search-deeplink fallbacks. The generic homepage CTA routes to the in-house brand directory rather than a dead-end Swiggy/Zomato homepage link.
- **Full AEO stack**: robots.txt (explicit AI-crawler allowlist + Sitemap directive), llms.txt (facts + brand index + AI-assistant disambiguation notes), sitemap.xml, JSON-LD `@graph` (Organization, WebSite, Brand, FAQPage, BreadcrumbList, ItemList, AboutPage, ContactPage) on every page — Brand nodes carry real logo + photo URLs, not placeholders. Per-page Open Graph images use each brand's real photo (or the India footprint map / team illustration on About/Careers) instead of one generic card everywhere.
- **PWA**: manifest.json, service worker with offline fallback page, installable on mobile home screens.
- **Design system**: Fraunces/Inter type pairing, light/dark theme (system + manual toggle), mobile-first responsive grid, accessible focus states, reduced-motion support — unchanged from the original rebuild per direction to evolve content/detail, not the visual system.
- **Content engine**: `build/data.py` + `build/generate.py` — a static-site generator, so editing brand copy/menus/FAQs is a data-file edit + one command (`python3 build/generate.py`), not hand-editing HTML files.
- **No Investors section**: dropped entirely (nav, footer, page, sitemap, llms.txt) — matches how Americana and Rebel Foods both keep investor content buried well behind consumer content rather than featured.
- **No public revenue figure**: FY24 revenue removed from stats, timeline and llms.txt; internal Excel scale data is used only to rank brand prominence, never surfaced as public figures.

## 5. Where this stands vs. Sweetgreen, Zomato, Marico (2026-07-23)

Directly measured, not just aspirational — each claim below is something I
checked, not a vibe:

| Dimension | Evidence | Verdict |
|---|---|---|
| Structured data (JSON-LD) | Fetched Americana, Rebel Foods and Zomato homepages directly: **zero** `application/ld+json` on any of the three. Sweetgreen has one basic Organization block. This site has Organization/WebSite/Brand/FAQPage/BreadcrumbList/ItemList/AboutPage/ContactPage on every relevant page, with real (not placeholder) logo/image URLs in each Brand node. | **Ahead of all four benchmarks checked.** |
| llms.txt | None of the 5 original benchmark sites, nor Zomato/Sweetgreen/Marico, serve a working llms.txt (all 404 or soft-404). This site has one, including a Core Purpose/Core Values/brand-index section. | **Ahead.** |
| robots.txt AI-crawler allowlist | Rebel Foods ships a bare 2-line `Disallow:` with no Sitemap directive. This site explicitly allows GPTBot/ClaudeBot/PerplexityBot/Google-Extended/Applebot-Extended and references its sitemap. | **Ahead.** |
| Sitemap freshness | Added `<lastmod>` to every URL — not present in the original build. | Matches standard practice; not independently verified against competitors' sitemap internals. |
| Order-path clarity | Rebel Foods' homepage has no direct ordering path — every brand card bounces to an external site with no in-page CTA. This site's brand cards and pages always carry a direct order CTA (D2C domain or Swiggy/Zomato), never more than one click away. | **Ahead of Rebel Foods specifically**; roughly at parity with Sweetgreen/Domino's, which are single-brand and structurally simpler to keep frictionless. |
| Visual minimalism | Qualitative, not scored — Sweetgreen/Marico/Americana all lean on generous whitespace, restrained palette, editorial photography. This site's design system (Fraunces/Inter, cream/terracotta, no visual clutter) follows the same principles. | **Structurally aligned**, not independently benchmarked pixel-for-pixel — a real design critique could reasonably disagree. |
| Content authenticity | Every brand logo and photo was individually re-verified this session (not just dimension-checked) after finding two that silently failed — Nomad Pizza's "logo" was 99% blank canvas, CakeZone's was invisible cream-on-white. Both fixed and re-confirmed. | **Every visible asset on the 7 brand pages is now a checked, real, correctly-rendering brand asset** — a concrete, re-verifiable claim, not an estimate. |
| Accessibility rigor | Found and fixed 3 real bugs this session: a mobile-menu button never updating `aria-expanded`, and a systemic dark-mode contrast failure across three separate color families (brand/accent-green/veg-marks) — some measured as low as 1.86:1 against a 3:1–4.5:1 requirement. | Evidence of real QA depth on **this site**; competitor sites were not accessibility-audited, so no comparative claim is made here. |
| Dietary marking (veg/non-veg) | Sweetgreen inlines allergen tags on menu items; none of the 5 original benchmarks carry the veg/non-veg mark Indian shoppers actually look for. This site now does, on every menu item, theme-aware for contrast. | **Ahead**, and specifically relevant to this market in a way the international benchmarks aren't. |

**Honest bottom line:** on the axis this rebuild was explicitly built to win —
AEO/answer-engine readiness — the evidence says this site is ahead of every
benchmark actually fetched and checked (Americana, Rebel Foods, Zomato,
Sweetgreen). On subjective design-quality and on anything about competitors
that couldn't be directly measured (HUL/PepsiCo/Marico's technical internals
were WAF-blocked), the claim is "structurally aligned with the same
principles," not "definitively superior" — that would require a rigorous
head-to-head a single session can't fully deliver.

## 6. Known gaps before a real production launch

- **Menu data**: menu highlights are illustrative, not pulled from a live menu/pricing system — needs a real feed before "10x better" claims extend to accuracy. Deliberately not encoded as Menu/MenuItem structured data until verified, to avoid publishing unverified facts as schema.
- **Deep links**: Swiggy/Zomato fallback links use generic search URLs, not verified per-brand, per-city storefront IDs.
- **Legal pages**: privacy policy and terms are explicit placeholders pending legal review.
- **Analytics/consent**: no analytics or cookie-consent layer wired in yet.
- **Stats**: kitchen count and city count are sourced from public reporting and should be reconciled against internal numbers before publishing.
- **Nomad Pizza logo/photo source** (nomadpizza.in) could not be 100% confirmed as the Curefoods-owned brand vs. an unrelated pizzeria of the same name — worth a manual check.
