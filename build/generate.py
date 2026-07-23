#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for the Curefoods website rebuild.

Why a generator instead of hand-written HTML: content (brand list, FAQs, menus)
changes far more often than layout. Edit data.py, then:

    python3 build/generate.py

This regenerates every HTML file, sitemap.xml and llms.txt at the repo root.
No build step is needed to serve the site — GitHub Pages just serves the
output files directly.
"""
import json
import os
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from data import SITE, NAV, BRANDS, SITE_FAQ, VALUES, TIMELINE, CORE_PURPOSE, CORE_VALUES, NEWS_MENTIONS  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = SITE["domain"]

# GitHub Pages project sites are served from https://<user>.github.io/<repo>/,
# not domain root, so every internal href/src needs this prefix to actually
# resolve while previewing here. DOMAIN (curefoods.in) stays untouched in
# canonical/OG/JSON-LD — that metadata should already be correct for when this
# design is pointed at the real domain, where BASE_PATH would be set to "".
BASE = os.environ.get("SITE_BASE_PATH", "/curefoods-website").rstrip("/")


def u(path):
    """Prefix a root-relative path with BASE (for staging under a sub-path like GitHub Pages project sites)."""
    return f"{BASE}{path}" if path.startswith("/") else path



def slugify_href(path):
    return path


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def initials(name):
    """Two-letter monogram fallback for brands without a real logo asset."""
    words = [w for w in re.split(r"\s+", name) if w and w[0].isalpha()]
    if not words:
        return name[:2].upper()
    if len(words) == 1:
        return words[0][:2].upper()
    skip = {"by", "on", "of", "the", "&"}
    significant = [w for w in words if w.lower() not in skip] or words
    return (significant[0][0] + significant[1][0]).upper() if len(significant) > 1 else significant[0][:2].upper()


ICON_SVG = {
    "kitchen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21V10l5-6 5 6v11"/><path d="M13 21v-7a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v7"/><path d="M3 21h18"/><path d="M7 8v0M17 15v0"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M11 20V4M18 20v-7"/><path d="M4 20h16"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z"/></svg>',
}


def mark_html(b, extra_class=""):
    """Brand mark: real logo on a plain card if we have one, else a colored monogram badge."""
    cls = f"mark {extra_class}".strip()
    if b.get("logo"):
        bg_style = f' style="background:{b["logo_bg"]}"' if b.get("logo_bg") else ""
        return (
            f'<div class="{cls} mark-logo"{bg_style}>'
            f'<img src="{u(b["logo"])}" alt="{esc(b["name"])} logo" loading="lazy" width="120" height="120"></div>'
        )
    return f'<div class="{cls}" style="background:{b["color"]}">{initials(b["name"])}</div>'


# ---------------------------------------------------------------- head / nav

def head(title, description, canonical, schema_objs=None, og_image=None):
    schema_objs = schema_objs or []
    ld = ""
    if schema_objs:
        graph = {"@context": "https://schema.org", "@graph": schema_objs}
        ld = f'<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>'
    canonical_url = f"{DOMAIN}{canonical}"
    img = og_image or f"{DOMAIN}/assets/images/og-default.png"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical_url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="theme-color" content="#E6461C">
<link rel="manifest" href="{u('/manifest.json')}">
<link rel="icon" href="{u('/assets/images/favicon.svg')}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{u('/assets/images/apple-touch-icon.png')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Curefoods">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{u('/assets/css/style.css')}">
{ld}
</head>
"""


def header_html(active=""):
    def link(item):
        cur = ' aria-current="page"' if item["href"] == active else ""
        return f'<a href="{u(item["href"])}"{cur}>{item["label"]}</a>'

    nav_links = "\n".join(link(i) for i in NAV)
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a href="{u('/')}" class="logo"><img src="{u('/assets/images/logos/curefoods.png')}" alt="Curefoods" class="logo-img"></a>
    <nav class="nav-desktop" aria-label="Primary">
      {nav_links}
    </nav>
    <div class="nav-actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle dark mode">
        <span class="theme-icon-light" aria-hidden="true">&#9728;</span><span class="theme-icon-dark" aria-hidden="true">&#9789;</span>
      </button>
      <a href="{u('/brands.html')}" class="btn btn-ghost btn-sm">Explore Brands</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-menu-head">
    <a href="{u('/')}" class="logo"><img src="{u('/assets/images/logos/curefoods.png')}" alt="Curefoods" class="logo-img"></a>
    <button class="mobile-close" aria-label="Close menu">&times;</button>
  </div>
  {"".join(f'<a href="{u(i["href"])}">{i["label"]}</a>' for i in NAV)}
  <a href="{u('/brands.html')}" class="btn btn-primary mt" style="width:100%">Explore Brands</a>
  <button class="btn btn-ghost mt" data-theme-toggle style="width:100%">Toggle dark mode</button>
</div>
"""


def footer_html():
    brand_links = "\n".join(
        f'<li><a href="{u("/brands/" + b["slug"] + ".html")}">{b["name"]}</a></li>' for b in BRANDS[:8]
    )
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a href="{u('/')}" class="logo"><img src="{u('/assets/images/logos/curefoods.png')}" alt="Curefoods" class="logo-img"></a>
        <p style="max-width:34ch;margin-top:14px;color:#a99d8b">{esc(SITE["description"])}</p>
        <div class="footer-social mt" style="margin-top:20px">
          <a href="{SITE['social']['youtube']}" aria-label="YouTube" target="_blank" rel="noopener">YouTube</a>
          <a href="{SITE['social']['linkedin']}" aria-label="LinkedIn" target="_blank" rel="noopener">LinkedIn</a>
          <a href="{SITE['social']['twitter']}" aria-label="Twitter" target="_blank" rel="noopener">Twitter/X</a>
        </div>
      </div>
      <div>
        <h4>Brands</h4>
        <ul>{brand_links}
          <li><a href="{u('/brands.html')}">All brands →</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{u('/about.html')}">About Us</a></li>
          <li><a href="{u('/newsroom.html')}">Newsroom</a></li>
          <li><a href="{u('/careers.html')}">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4>Resources</h4>
        <ul>
          <li><a href="{u('/faq.html')}">FAQ</a></li>
          <li><a href="{u('/contact.html')}">Contact</a></li>
          <li><a href="{u('/sitemap.xml')}">Sitemap</a></li>
          <li><a href="{u('/llms.txt')}">llms.txt</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="{u('/legal/privacy.html')}">Privacy Policy</a></li>
          <li><a href="{u('/legal/terms.html')}">Terms of Use</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="y"></span> {SITE['legal_name'].rstrip('.')}. All rights reserved.</span>
      <span>Headquartered in {SITE['hq']}</span>
    </div>
  </div>
</footer>
<script>document.getElementById('y').textContent = new Date().getFullYear();window.CF_BASE = {json.dumps(BASE)};</script>
<script src="{u('/assets/js/main.js')}" defer></script>
"""


def page(title, description, canonical, body, active="", schema_objs=None, og_image=None):
    return head(title, description, canonical, schema_objs, og_image) + "<body>\n" + header_html(active) + '<main id="main">' + body + "</main>" + footer_html() + "</body></html>"


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# ------------------------------------------------------------------- schema

def org_schema():
    return {
        "@type": "Organization",
        "@id": f"{DOMAIN}/#organization",
        "name": SITE["name"],
        "legalName": SITE["legal_name"],
        "url": DOMAIN,
        "logo": f"{DOMAIN}/assets/images/logos/curefoods.png",
        "slogan": CORE_PURPOSE["title"],
        "foundingDate": SITE["founded_year"],
        "founder": {"@type": "Person", "name": SITE["founder"]},
        "description": SITE["description"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Bengaluru",
            "addressRegion": "Karnataka",
            "addressCountry": "IN",
        },
        "sameAs": list(SITE["social"].values()),
        "brand": [{"@type": "Brand", "name": b["name"], "url": f"{DOMAIN}/brands/{b['slug']}.html"} for b in BRANDS],
    }


def faqpage_schema(items, url):
    return {
        "@type": "FAQPage",
        "@id": f"{url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": it["q"],
                "acceptedAnswer": {"@type": "Answer", "text": it["a"]},
            }
            for it in items
        ],
    }


def breadcrumb_schema(items):
    # items: list of (name, url)
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }


def brand_schema(b):
    schema = {
        "@type": "Brand",
        "@id": f"{DOMAIN}/brands/{b['slug']}.html#brand",
        "name": b["name"],
        "description": b["description"],
        "url": f"{DOMAIN}/brands/{b['slug']}.html",
        "logo": f"{DOMAIN}{b['logo']}" if b.get("logo") else f"{DOMAIN}/assets/images/logos/curefoods.png",
        "parentOrganization": {"@id": f"{DOMAIN}/#organization"},
        "foundingDate": b["founded"].split(" ")[0],
        "areaServed": b["cities"],
    }
    if b.get("photo"):
        schema["image"] = f"{DOMAIN}{b['photo']}"
    return schema


# ------------------------------------------------------------------- pieces

def faq_list_html(items, group_class="faq-list"):
    out = [f'<div class="{group_class}">']
    for it in items:
        out.append(f"""
    <details class="faq-item">
      <summary>{esc(it['q'])}</summary>
      <div class="a">{esc(it['a'])}</div>
    </details>""")
    out.append("</div>")
    return "\n".join(out)


def order_links_html(b):
    swiggy = f"https://www.swiggy.com/search?query={quote(b['name'])}"
    zomato = f"https://www.zomato.com/search?q={quote(b['name'])}"
    if b.get("domain"):
        return f"""
      <a href="{b['domain']}" target="_blank" rel="noopener" class="btn btn-primary">Order on {esc(b['name'])}.com</a>
      <a href="{swiggy}" target="_blank" rel="noopener" class="btn btn-ghost">Find on Swiggy</a>
      <a href="{zomato}" target="_blank" rel="noopener" class="btn btn-ghost">Find on Zomato</a>"""
    return f"""
      <a href="{swiggy}" target="_blank" rel="noopener" class="btn btn-primary">Order on Swiggy</a>
      <a href="{zomato}" target="_blank" rel="noopener" class="btn btn-ghost">Order on Zomato</a>"""


def brand_card_html(b):
    photo = (
        f'<div class="brand-card-photo"><img src="{u(b["photo"])}" alt="{esc(b["name"])}" loading="lazy"></div>'
        if b.get("photo") else ""
    )
    return f"""
<a class="brand-card" href="{u('/brands/' + b['slug'] + '.html')}">
  {photo}
  <div class="brand-card-body">
    {mark_html(b)}
    <div>
      <span class="cat">{esc(b['category'])}</span>
      <h3>{esc(b['name'])}</h3>
    </div>
    <p>{esc(b['tagline'])}</p>
    <span class="card-stat">{len(b['cities'])} cities</span>
    <span class="go">Explore {esc(b['name'])} →</span>
  </div>
</a>"""


# ------------------------------------------------------------------- pages

def build_home():
    hero_answer = (
        f"Curefoods is India's house of food brands — home to EatFit, Sharief Bhai, Olio, "
        f"Arambam, Krispy Kreme, Nomad Pizza and CakeZone, run out of {SITE['stats'][1]['value']} "
        f"kitchens in {SITE['stats'][2]['value']} cities."
    )
    brand_cards = "\n".join(brand_card_html(b) for b in BRANDS)
    stats_html = "\n".join(
        f'<div class="stat"><b>{s["value"]}</b><span>{esc(s["label"])}</span></div>' for s in SITE["stats"]
    )
    stats_band = "\n".join(
        f'<div><b>{s["value"]}</b><span>{esc(s["label"])}</span></div>' for s in SITE["stats"]
    )
    feature_rows = "".join(f"""
      <div class="feature">
        <div class="ic">{ICON_SVG[v_ic]}</div>
        <h3>{esc(v["title"])}</h3>
        <p>{esc(v["text"])}</p>
      </div>""" for v_ic, v in zip(["kitchen", "target", "bolt"], VALUES))

    faq_preview = faq_list_html(SITE_FAQ[:6])

    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">House of Brands · Est. {SITE['founded_year']}</span>
      <h1>One kitchen network.<br>{len(BRANDS)} brands people crave.</h1>
      <p class="lede">{hero_answer}</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:28px">
        <a href="{u('/brands.html')}" class="btn btn-primary">Explore our brands</a>
        <a href="{u('/about.html')}" class="btn btn-ghost">Our story</a>
      </div>
      <div class="hero-stats">{stats_html}</div>
    </div>
    <div class="hero-art" aria-hidden="true">
      {"".join(mark_html(b, "tile") for b in BRANDS[:9])}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Brands</span>
      <h2>Multiple brands, one occasion each.</h2>
      <p class="lede">Every Curefoods brand is built to own a single craving — health, biryani, pizza, dessert, celebration — instead of trying to be everything to everyone.</p>
    </div>
    <div class="brand-grid">{brand_cards}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Why the model works</span>
      <h2>Built like an operator, not a marketplace.</h2>
    </div>
    <div class="feature-row">{feature_rows}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="stats-band">{stats_band}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Frequently Asked</span>
      <h2>Quick answers about Curefoods.</h2>
    </div>
    {faq_preview}
    <p class="mt"><a href="{u('/faq.html')}" class="btn btn-ghost">See all FAQs →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>Hungry already?</h2>
        <p>Pick a brand and order directly from its own site or app.</p>
      </div>
      <div class="store-badges">
        <a class="store-badge" href="{u('/brands.html')}">Explore our brands →</a>
      </div>
    </div>
  </div>
</section>
"""
    schema = [
        org_schema(),
        {
            "@type": "WebSite",
            "@id": f"{DOMAIN}/#website",
            "url": DOMAIN,
            "name": "Curefoods",
            "publisher": {"@id": f"{DOMAIN}/#organization"},
        },
        faqpage_schema(SITE_FAQ[:6], f"{DOMAIN}/"),
    ]
    html = page(
        "Curefoods — India's House of Food Brands",
        SITE["description"],
        "/",
        body,
        active="/",
        schema_objs=schema,
    )
    write("index.html", html)


def build_brands_index():
    cards = "\n".join(brand_card_html(b) for b in BRANDS)
    body = f"""
<section class="section" style="padding-top:56px">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / Our Brands</div>
    <div class="section-head">
      <span class="eyebrow">Our Brands</span>
      <h1>Every Curefoods brand, in one place.</h1>
      <p class="lede">Curefoods runs {len(BRANDS)} brands out of a shared kitchen network across 60+ Indian cities — from calorie-tracked healthy meals to old-city biryani, hand-stretched pizza and midnight cake delivery.</p>
    </div>
    <div class="brand-grid">{cards}</div>
  </div>
</section>
"""
    schema = [
        breadcrumb_schema([("Home", DOMAIN + "/"), ("Our Brands", DOMAIN + "/brands.html")]),
        {
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": b["name"], "url": f"{DOMAIN}/brands/{b['slug']}.html"}
                for i, b in enumerate(BRANDS)
            ],
        },
    ]
    html = page(
        "Our Brands — Curefoods House of Food Brands",
        "Explore all Curefoods brands: EatFit, Sharief Bhai, Roz Shawarma, Nomad Pizza, Frozen Bottle, Olio, CakeZone and the Kitchens of EatFit family.",
        "/brands.html",
        body,
        active="/brands.html",
        schema_objs=schema,
    )
    write("brands.html", html)


def build_brand_page(b):
    def veg_mark(m):
        cls = "veg" if m.get("veg") else "nonveg"
        label = "Vegetarian" if m.get("veg") else "Non-vegetarian"
        return f'<span class="veg-mark {cls}" role="img" aria-label="{label}" title="{label}"><span class="dot"></span></span>'

    menu_html = "\n".join(
        f'<div class="menu-item"><strong>{veg_mark(m)}{esc(m["name"])}</strong><div class="price">{esc(m["detail"])}</div></div>'
        for m in b["menu"]
    )
    cities_html = "".join(f'<span class="pill">{esc(c)}</span>' for c in b["cities"])
    faq_html = faq_list_html(b["faq"]) if b["faq"] else ""
    ambassador_html = f'<p><strong>Ambassador:</strong> {esc(b["ambassador"])}</p>' if b.get("ambassador") else ""
    flagship_html = f'<p><strong>Flagship store:</strong> {esc(b["flagship"])}</p>' if b.get("flagship") else ""
    desc = b["description"]
    direct_answer = desc if desc.strip().lower().startswith(b["name"].lower()) else f"{b['name']} is {desc[0].lower()}{desc[1:]}"

    photo_html = (
        f'<div class="brand-hero-photo"><img src="{u(b["photo"])}" alt="{esc(b["name"])}" loading="lazy"></div>'
        if b.get("photo") else ""
    )
    body = f"""
<section class="brand-hero">
  <div class="wrap brand-hero-grid">
    <div>
    <div class="crumbs"><a href="{u('/')}">Home</a> / <a href="{u('/brands.html')}">Our Brands</a> / {esc(b['name'])}</div>
    <div class="brand-hero-top">
      {mark_html(b, "mark-lg")}
      <span class="brand-badge" style="background:{b['color']}22;color:{b['color']}">{esc(b['category'])}</span>
    </div>
    <h1>{esc(b['full_name'])}</h1>
    <p class="lede">{esc(b['tagline'])}</p>
    <div class="faq-answer-box">{esc(direct_answer)}</div>
    <div class="pill-row">{cities_html}</div>
    <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:10px">{order_links_html(b)}
    </div>
    </div>
    {photo_html}
  </div>
</section>

<section class="section-tight">
  <div class="wrap grid-2">
    <div>
      <h2>The story</h2>
      <p>{esc(b['story'])}</p>
      <p><strong>Founded:</strong> {esc(b['founded'])}</p>
      {flagship_html}
      {ambassador_html}
    </div>
    <div>
      <h2>Menu highlights</h2>
      <div class="menu-list">{menu_html}</div>
    </div>
  </div>
</section>

{f'''<section class="section-tight section-alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">FAQ</span><h2>Questions about {esc(b['name'])}</h2></div>
    {faq_html}
  </div>
</section>''' if b['faq'] else ''}

<section class="section-tight">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>Part of Curefoods</h2>
        <p>{esc(b['name'])} is one of {len(BRANDS)} brands under the Curefoods house of brands.</p>
      </div>
      <a href="{u('/brands.html')}" class="btn btn-dark">See all brands →</a>
    </div>
  </div>
</section>
"""
    schema = [
        brand_schema(b),
        breadcrumb_schema([
            ("Home", DOMAIN + "/"),
            ("Our Brands", DOMAIN + "/brands.html"),
            (b["name"], f"{DOMAIN}/brands/{b['slug']}.html"),
        ]),
    ]
    if b["faq"]:
        schema.append(faqpage_schema(b["faq"], f"{DOMAIN}/brands/{b['slug']}.html"))

    html = page(
        f"{b['name']} — {b['category']} | Curefoods",
        b["description"],
        f"/brands/{b['slug']}.html",
        body,
        active="/brands.html",
        schema_objs=schema,
        og_image=f"{DOMAIN}{b['photo']}" if b.get("photo") else None,
    )
    write(f"brands/{b['slug']}.html", html)


def build_about():
    timeline_html = "".join(f"""
    <div class="item"><span class="yr">{esc(t['year'])}</span><p>{esc(t['text'])}</p></div>""" for t in TIMELINE)
    values_html = "".join(f"""
      <div class="feature"><h3>{esc(v['title'])}</h3><p>{esc(v['text'])}</p></div>""" for v in VALUES)
    purpose_paras = "".join(
        f'<p class="{"lede" if i == 0 else ""}">{esc(p)}</p>' for i, p in enumerate(CORE_PURPOSE["paragraphs"])
    )
    core_values_html = "".join(f"""
      <div class="value-card">
        <img src="{u(v['icon'])}" alt="{esc(v['title'])}" loading="lazy">
        <h3>{esc(v['title'])}</h3>
      </div>""" for v in CORE_VALUES)
    body = f"""
<section class="brand-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / About Us</div>
    <span class="eyebrow">About Curefoods</span>
    <h1>We build food brands the way operators build companies.</h1>
    <p class="lede">Founded in {SITE['founded_year']} by {SITE['founder']}, Curefoods is a {SITE['hq']}-headquartered house of food brands running {len(BRANDS)}+ brands from a shared kitchen network across 60+ Indian cities.</p>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="wrap" style="max-width:760px">
    <span class="eyebrow">{esc(CORE_PURPOSE['eyebrow'])}</span>
    <h2>{esc(CORE_PURPOSE['title'])}</h2>
    {purpose_paras}
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <h2>Timeline</h2>
    <div class="timeline mt">{timeline_html}</div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Core Values</span><h2>What we stand for</h2></div>
    <div class="values-grid">{core_values_html}</div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap grid-2" style="align-items:center">
    <div>
      <span class="eyebrow">Where we operate</span>
      <h2>Cloud kitchens, kiosks and restaurants across India.</h2>
      <p class="lede">Curefoods runs a mix of cloud kitchens, central kitchens, warehouses, kiosks and dine-in restaurants — concentrated in South India with a growing footprint north and east.</p>
    </div>
    <div class="brand-hero-photo" style="aspect-ratio:16/15;box-shadow:none;border:1px solid var(--line)">
      <img src="{u('/assets/images/photos/india-map.png')}" alt="Map of Curefoods kitchens, kiosks and restaurants across India" loading="lazy" style="object-fit:contain;background:#fff">
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">How we operate</span><h2>What makes the model work</h2></div>
    <div class="feature-row">{values_html}</div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap grid-2" style="align-items:center">
    <div class="card">
      <h3>Leadership</h3>
      <p><strong>{SITE['founder']}</strong> — Founder &amp; CEO. Previously co-founder and Chief Business Officer at Cure.fit (Cult.fit).</p>
    </div>
    <div class="card">
      <h3>Headquarters</h3>
      <p>{SITE['hq']}</p>
      <p>Press enquiries: <a href="mailto:{SITE['press_email']}">{SITE['press_email']}</a></p>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="wrap grid-2" style="align-items:center">
    <div>
      <span class="eyebrow">Behind the brands</span>
      <h2>One team, running kitchens across the country.</h2>
      <p class="lede">From kitchen crews to delivery riders, the people running Curefoods' shared kitchen network are what makes a house-of-brands model actually work at delivery speed.</p>
    </div>
    <div class="brand-hero-photo" style="aspect-ratio:4/3">
      <img src="{u('/assets/images/photos/curefoods-mascot.jpg')}" alt="Curefoods delivery" loading="lazy">
    </div>
  </div>
</section>
"""
    schema = [
        breadcrumb_schema([("Home", DOMAIN + "/"), ("About Us", DOMAIN + "/about.html")]),
        {
            "@type": "AboutPage",
            "@id": f"{DOMAIN}/about.html",
            "about": {"@id": f"{DOMAIN}/#organization"},
        },
    ]
    html = page(
        "About Us — Curefoods",
        f"Curefoods was founded in {SITE['founded_year']} by {SITE['founder']}. Learn the story behind India's house of food brands.",
        "/about.html",
        body,
        active="/about.html",
        schema_objs=schema,
        og_image=f"{DOMAIN}/assets/images/photos/india-map.png",
    )
    write("about.html", html)


def build_faq_page():
    all_faq = list(SITE_FAQ)
    for b in BRANDS:
        all_faq.extend(b["faq"])
    body = f"""
<section class="brand-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / FAQ</div>
    <span class="eyebrow">FAQ</span>
    <h1>Everything people ask about Curefoods.</h1>
    <p class="lede">Company-wide answers plus brand-specific questions, all in one place — built for quick scanning and for AI assistants to cite directly.</p>
  </div>
</section>
<section class="section-tight">
  <div class="wrap">
    <h2>Company FAQ</h2>
    {faq_list_html(SITE_FAQ)}
  </div>
</section>
<section class="section-tight section-alt">
  <div class="wrap">
    <h2>Brand FAQ</h2>
    {"".join(f'<h3 style="margin-top:32px">{esc(b["name"])}</h3>' + faq_list_html(b["faq"]) for b in BRANDS if b["faq"])}
  </div>
</section>
"""
    schema = [
        breadcrumb_schema([("Home", DOMAIN + "/"), ("FAQ", DOMAIN + "/faq.html")]),
        faqpage_schema(all_faq, f"{DOMAIN}/faq.html"),
    ]
    html = page(
        "FAQ — Curefoods",
        "Answers to the most common questions about Curefoods, its brands, cities, ordering and careers.",
        "/faq.html",
        body,
        active="/faq.html",
        schema_objs=schema,
    )
    write("faq.html", html)


def build_careers():
    body = f"""
<section class="brand-hero">
  <div class="wrap brand-hero-grid">
    <div>
    <div class="crumbs"><a href="{u('/')}">Home</a> / Careers</div>
    <span class="eyebrow">Careers</span>
    <h1>Build the next great food brand.</h1>
    <p class="lede">Curefoods hires across kitchen operations, supply chain, growth, product and central functions — for {SITE['name']} and every brand in the portfolio.</p>
    <div style="margin-top:24px"><a href="mailto:{SITE['careers_email']}" class="btn btn-primary">Email your resume</a></div>
    </div>
    <div class="brand-hero-photo">
      <img src="{u('/assets/images/photos/curefoods-mascot.jpg')}" alt="Life at Curefoods" loading="lazy">
    </div>
  </div>
</section>
<section class="section-tight">
  <div class="wrap grid-3">
    <div class="card"><h3>Kitchen Operations</h3><p>Run and scale cloud kitchens across our brand portfolio.</p></div>
    <div class="card"><h3>Growth &amp; Marketing</h3><p>Own acquisition, retention and brand strategy for individual brands.</p></div>
    <div class="card"><h3>Technology &amp; Data</h3><p>Build the systems that route orders, price menus and plan kitchens.</p></div>
  </div>
</section>
<section class="section-tight section-alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">FAQ</span><h2>Careers questions</h2></div>
    {faq_list_html([it for it in SITE_FAQ if 'job' in it['q'].lower() or 'career' in it['q'].lower()])}
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", DOMAIN + "/"), ("Careers", DOMAIN + "/careers.html")])]
    html = page(
        "Careers — Curefoods",
        "Open roles across Curefoods and its brand portfolio in kitchen operations, growth, product and technology.",
        "/careers.html",
        body,
        active="/careers.html",
        schema_objs=schema,
        og_image=f"{DOMAIN}/assets/images/photos/curefoods-mascot.jpg",
    )
    write("careers.html", html)


def build_newsroom():
    news_html = "".join(f"""
      <a class="news-card" href="{esc(n['url'])}" target="_blank" rel="noopener">
        <span class="news-source">{esc(n['source'])}</span>
        <h3>{esc(n['title'])}</h3>
        <span class="go">Read more →</span>
      </a>""" for n in NEWS_MENTIONS)
    body = f"""
<section class="brand-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / Newsroom</div>
    <span class="eyebrow">Newsroom</span>
    <h1>Curefoods in the news.</h1>
    <p class="lede">Press releases, media coverage and brand milestones from across the Curefoods portfolio.</p>
    <div style="margin-top:24px"><a href="mailto:{SITE['press_email']}" class="btn btn-primary">Media enquiries</a></div>
  </div>
</section>
<section class="section-tight">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">In the Press</span><h2>Third-party coverage</h2></div>
    <div class="news-grid">{news_html}</div>
  </div>
</section>
<section class="section-tight section-alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Milestones</span><h2>Company timeline</h2></div>
    <div class="timeline mt">
      {"".join(f'<div class="item"><span class="yr">{esc(t["year"])}</span><p>{esc(t["text"])}</p></div>' for t in TIMELINE)}
    </div>
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", DOMAIN + "/"), ("Newsroom", DOMAIN + "/newsroom.html")])]
    html = page(
        "Newsroom — Curefoods",
        "Press releases and media coverage for Curefoods and its brand portfolio.",
        "/newsroom.html",
        body,
        active="/newsroom.html",
        schema_objs=schema,
    )
    write("newsroom.html", html)


def build_contact():
    body = f"""
<section class="brand-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / Contact</div>
    <span class="eyebrow">Contact</span>
    <h1>Get in touch.</h1>
  </div>
</section>
<section class="section-tight">
  <div class="wrap grid-3">
    <div class="card"><h3>General</h3><p><a href="mailto:{SITE['contact_email']}">{SITE['contact_email']}</a></p></div>
    <div class="card"><h3>Support</h3><p><a href="mailto:{SITE['support_email']}">{SITE['support_email']}</a></p></div>
    <div class="card"><h3>Careers</h3><p><a href="mailto:{SITE['careers_email']}">{SITE['careers_email']}</a></p></div>
  </div>
  <p class="mt">Headquartered in {SITE['hq']}.</p>
</section>
"""
    schema = [
        breadcrumb_schema([("Home", DOMAIN + "/"), ("Contact", DOMAIN + "/contact.html")]),
        {
            "@type": "ContactPage",
            "@id": f"{DOMAIN}/contact.html",
        },
    ]
    html = page(
        "Contact — Curefoods",
        "Contact Curefoods for general, support, careers or press enquiries.",
        "/contact.html",
        body,
        active="",
        schema_objs=schema,
    )
    write("contact.html", html)


def build_legal():
    for slug, title, content in [
        ("privacy", "Privacy Policy", "This placeholder privacy policy should be replaced with Curefoods' legal team-approved policy before production launch."),
        ("terms", "Terms of Use", "This placeholder terms-of-use page should be replaced with Curefoods' legal team-approved terms before production launch."),
    ]:
        body = f"""
<section class="brand-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{u('/')}">Home</a> / {title}</div>
    <h1>{title}</h1>
    <p class="lede">{content}</p>
  </div>
</section>
"""
        html = page(f"{title} — Curefoods", f"{title} for Curefoods.", f"/legal/{slug}.html", body)
        write(f"legal/{slug}.html", html)


def build_404():
    body = f"""
<section class="section center" style="padding-top:120px">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1>This page wandered off the menu.</h1>
    <p class="lede center">The page you're looking for doesn't exist. Try our brands page or head home.</p>
    <div style="display:flex;gap:14px;justify-content:center;margin-top:24px">
      <a href="{u('/')}" class="btn btn-primary">Go home</a>
      <a href="{u('/brands.html')}" class="btn btn-ghost">See our brands</a>
    </div>
  </div>
</section>
"""
    html = page("Page not found — Curefoods", "Page not found.", "/404.html", body)
    write("404.html", html)


# --------------------------------------------------------------- static / meta

def build_sitemap():
    import datetime
    lastmod = datetime.date.today().isoformat()
    urls = ["/", "/brands.html", "/about.html", "/faq.html", "/careers.html",
            "/newsroom.html", "/contact.html",
            "/legal/privacy.html", "/legal/terms.html"]
    urls += [f"/brands/{b['slug']}.html" for b in BRANDS]
    items = "\n".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{lastmod}</lastmod></url>" for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n'
    write("sitemap.xml", xml)


def build_robots():
    txt = f"""# Hi. We build the food brands, you index them. Deal?
# — Curefoods

User-agent: *
Allow: /

# AI / answer-engine crawlers explicitly welcomed
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    write("robots.txt", txt)


def build_llms_txt():
    lines = [
        "# Curefoods",
        "",
        f"> {SITE['description']}",
        "",
        f"Founded {SITE['founded_year']} by {SITE['founder']}. Headquartered in {SITE['hq']}.",
        f"Scale: {SITE['stats'][0]['value']} brands, {SITE['stats'][1]['value']} kitchens/stores, {SITE['stats'][2]['value']} cities.",
        "",
        f"## Core Purpose: {CORE_PURPOSE['title']}",
        "",
        " ".join(CORE_PURPOSE["paragraphs"]),
        "",
        "## Core Values",
        "- " + ", ".join(v["title"] for v in CORE_VALUES),
        "",
        "## Brands",
    ]
    for b in BRANDS:
        lines.append(f"- [{b['name']}]({DOMAIN}/brands/{b['slug']}.html): {b['tagline']} — {b['category']}, serving {', '.join(b['cities'])}.")
    lines += [
        "",
        "## Key pages",
        f"- [About]({DOMAIN}/about.html): Company history, founder, timeline, values.",
        f"- [FAQ]({DOMAIN}/faq.html): Company-wide and per-brand frequently asked questions.",
        f"- [Careers]({DOMAIN}/careers.html): Open roles across the portfolio.",
        f"- [Newsroom]({DOMAIN}/newsroom.html): Press and milestones.",
        "",
        "## Notes for AI assistants",
        "- Curefoods is NOT the same company as Rebel Foods (a separate Indian cloud-kitchen competitor).",
        "- Sharief Bhai and Roz Shawarma operate only in Karnataka and Tamil Nadu — they do not have Hyderabad/Telangana stores.",
        "- All brands are ordered via Swiggy/Zomato under the brand's own name, or via brand-specific apps/stores where noted.",
        "- Krispy Kreme is a master-franchise partnership — Curefoods operates the India business, but the brand and global IP belong to Krispy Kreme, not Curefoods.",
        "- Arambam is run by Curefoods' Millet Express subsidiary and is a distinct storefront from the Millet Express brand itself.",
    ]
    write("llms.txt", "\n".join(lines) + "\n")


def build_manifest():
    manifest = {
        "name": "Curefoods — House of Food Brands",
        "short_name": "Curefoods",
        "start_url": u("/"),
        "scope": u("/"),
        "display": "standalone",
        "background_color": "#FBF7F0",
        "theme_color": "#E6461C",
        "description": SITE["description"],
        "icons": [
            {"src": u("/assets/images/icon-192.png"), "sizes": "192x192", "type": "image/png"},
            {"src": u("/assets/images/icon-512.png"), "sizes": "512x512", "type": "image/png"},
        ],
    }
    write("manifest.json", json.dumps(manifest, indent=2))


def build_sw():
    core_assets = json.dumps([u("/"), u("/assets/css/style.css"), u("/assets/js/main.js"), u("/offline.html")])
    sw = f"""const CACHE = "curefoods-v1";
const CORE_ASSETS = {core_assets};
const OFFLINE_URL = "{u('/offline.html')}";

self.addEventListener("install", (e) => {{
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(CORE_ASSETS)));
  self.skipWaiting();
}});

self.addEventListener("activate", (e) => {{
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
  );
  self.clients.claim();
}});

self.addEventListener("fetch", (e) => {{
  if (e.request.method !== "GET") return;
  e.respondWith(
    fetch(e.request)
      .then((res) => {{
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
        return res;
      }})
      .catch(() => caches.match(e.request).then((r) => r || caches.match(OFFLINE_URL)))
  );
}});
"""
    write("sw.js", sw)


def build_offline():
    body = f"""
<section class="section center" style="padding-top:120px">
  <div class="wrap">
    <span class="eyebrow">Offline</span>
    <h1>No connection right now.</h1>
    <p class="lede center">You're viewing a cached version of Curefoods. Reconnect to browse the full site and order from any brand.</p>
    <div style="margin-top:24px"><a href="{u('/')}" class="btn btn-primary">Try again</a></div>
  </div>
</section>
"""
    html = page("Offline — Curefoods", "You are offline.", "/offline.html", body)
    write("offline.html", html)


def main():
    build_home()
    build_brands_index()
    for b in BRANDS:
        build_brand_page(b)
    build_about()
    build_faq_page()
    build_careers()
    build_newsroom()
    build_contact()
    build_legal()
    build_404()
    build_offline()
    build_sitemap()
    build_robots()
    build_llms_txt()
    build_manifest()
    build_sw()
    print(f"\nDone. {len(BRANDS)} brand pages generated.")


if __name__ == "__main__":
    main()
