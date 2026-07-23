# -*- coding: utf-8 -*-
"""
Content data for the Curefoods website rebuild.
Edit this file to change copy/content, then run `python3 generate.py`.
"""

SITE = {
    "name": "Curefoods",
    "legal_name": "Curefoods India Pvt. Ltd.",
    "domain": "https://curefoods.in",
    "tagline": "India's house of food brands",
    "description": (
        "Curefoods is India's house of food brands, building and scaling "
        "category-defining F&B brands — from healthy meals to biryani, pizza to "
        "desserts — out of 281 cloud kitchens, 99 kiosks and 122 restaurants."
    ),
    "founder": "Ankit Nagori",
    "founded_year": "2020",
    "hq": "Bengaluru, Karnataka, India",
    "stats": [
        {"value": "281", "label": "Cloud kitchens"},
        {"value": "99", "label": "Kiosks"},
        {"value": "122", "label": "Restaurants"},
    ],
    "social": {
        "youtube": "https://www.youtube.com/@the_curefoods",
        "linkedin": "https://in.linkedin.com/company/curefoods",
        "twitter": "https://x.com/the_curefoods/",
    },
    "contact_email": "hello@curefoods.in",
    "support_email": "support@curefoods.in",
    "press_email": "press@curefoods.in",
    "careers_email": "careers@curefoods.in",
}

NAV = [
    {"label": "Our Brands", "href": "/brands.html"},
    {"label": "About Us", "href": "/about.html"},
    {"label": "Newsroom", "href": "/newsroom.html"},
    {"label": "Careers", "href": "/careers.html"},
    {"label": "FAQ", "href": "/faq.html"},
]

# Each brand: slug, name, category, color, short description, long story,
# menu highlights, cities, founded year, faq (brand-specific, feeds FAQPage schema)
BRANDS = [
    {
        "slug": "eatfit",
        "name": "EatFit",
        "full_name": "EatFit — Kitchens of EatFit",
        "category": "Healthy Meals",
        "color": "#1F6D4C",
        "logo": "/assets/images/logos/eatfit.png",
        "photo": "/assets/images/photos/eatfit-food.jpg",
        "tagline": "Calorie-counted meals for people who refuse to compromise.",
        "description": (
            "EatFit is Curefoods' flagship healthy-eating brand, delivering "
            "calorie-tracked, macro-balanced meals designed with nutritionists. "
            "It anchors the 'Kitchens of EatFit' umbrella of eight sister brands "
            "operating out of the same shared kitchens."
        ),
        "story": (
            "Founded as the first brand under Curefoods in 2020, EatFit set out to prove "
            "that healthy food could be convenient, affordable and genuinely tasty at scale. "
            "Every meal is nutrition-labelled with calories, protein and macros, and the menu "
            "rotates seasonally with dietitian input. In 2023, EatFit relaunched as 'Kitchens "
            "of EatFit', bringing HRX by EatFit, Great Indian Khichdi, Homeplate, Chaat Street, "
            "Rolls on Wheels, Millet Express and Madras Curd Rice Company onto one shared "
            "kitchen network — letting a single delivery batch carry dishes from multiple "
            "brands to the same customer."
        ),
        "menu": [
            {"veg": False, "name": "Peri Peri Chicken Rice Bowl", "detail": "420 kcal · 32g protein"},
            {"veg": True, "name": "Paneer Tikka Overload Bowl", "detail": "390 kcal · 24g protein"},
            {"veg": False, "name": "Grilled Chicken Salad", "detail": "310 kcal · 28g protein"},
            {"veg": True, "name": "Quinoa Khichdi", "detail": "340 kcal · 14g protein"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi NCR"],
        "founded": "2020",
        "ambassador": "Hrithik Roshan (brand ambassador & investor)",
        "faq": [
            {
                "q": "What makes EatFit different from a regular food delivery brand?",
                "a": "Every EatFit dish is nutrition-labelled with exact calories, protein, carbs and fat, "
                     "designed with dietitians so customers can hit fitness goals without home-cooking.",
            },
            {
                "q": "What is 'Kitchens of EatFit'?",
                "a": "Kitchens of EatFit is the shared-kitchen umbrella that houses EatFit alongside seven "
                     "sister brands — HRX by EatFit, Great Indian Khichdi, Homeplate, Chaat Street, Rolls on "
                     "Wheels, Millet Express and Madras Curd Rice Company — so one order can mix dishes from all of them.",
            },
            {
                "q": "Which cities is EatFit available in?",
                "a": "EatFit operates in Bengaluru, Hyderabad, Chennai, Mumbai and Delhi NCR, with kitchens "
                     "expanding as Curefoods opens new cloud-kitchen clusters.",
            },
        ],
    },
    {
        "slug": "sharief-bhai",
        "name": "Sharief Bhai",
        "full_name": "Sharief Bhai",
        "category": "Biryani & Mandi",
        "color": "#B8330F",
        "logo": "/assets/images/logos/sharief-bhai.png",
        "photo": "/assets/images/photos/sharief-bhai-store.jpg",
        "domain": "https://www.shariefbhai.com",
        "tagline": "Old-city biryani and Arabian mandi, done right.",
        "description": (
            "Sharief Bhai brings authentic Karnataka-style biryani, mandi and kebabs to "
            "delivery and dine-in, anchored by its flagship dine-in store on Mosque Road, "
            "Frazer Town, Bengaluru — the city's historic biryani street."
        ),
        "story": (
            "Sharief Bhai was built to capture the soul of Bengaluru's Mosque Road biryani "
            "culture — slow-cooked dum biryani, mandi and ghee rice — and take it city-wide "
            "without losing the recipe. The brand runs a growing lineup of ghee rice SKUs "
            "alongside its core biryani and mandi range, and operates a mix of delivery-only "
            "kitchens and dine-in flagship stores. Its sibling brand, Roz Shawarma, spun out "
            "to focus purely on shawarma and rolls for a faster, lighter occasion."
        ),
        "menu": [
            {"veg": False, "name": "Hyderabadi Chicken Dum Biryani", "detail": "Signature slow-dum biryani"},
            {"veg": False, "name": "Chicken Mandi", "detail": "Arabian-style rice & smoked chicken"},
            {"veg": True, "name": "Ghee Rice Combo", "detail": "Multiple ghee rice variants"},
            {"veg": False, "name": "Seekh Kebab Platter", "detail": "Char-grilled kebabs"},
        ],
        "cities": ["Bengaluru", "Chennai", "Coimbatore", "Mysore", "Mangalore", "Manipal", "Tumkur", "Hassan", "Puducherry", "Hosur"],
        "store_count": "54",
        "founded": "2021",
        "flagship": "Mosque Road, Frazer Town, Bengaluru",
        "faq": [
            {
                "q": "Where is Sharief Bhai's flagship store?",
                "a": "Sharief Bhai's flagship dine-in store is on Mosque Road in Frazer Town, Bengaluru — "
                     "the city's historic biryani and old-city food street.",
            },
            {
                "q": "Is Sharief Bhai available outside Karnataka?",
                "a": "Sharief Bhai runs 54 stores across 10 cities in Karnataka (Bengaluru, Mysore, "
                     "Mangalore, Manipal, Tumkur, Hassan), Tamil Nadu (Chennai, Coimbatore, Hosur) "
                     "and Puducherry — it does not currently have stores in Hyderabad or the rest "
                     "of Telangana.",
            },
            {
                "q": "What is the difference between Sharief Bhai and Roz Shawarma?",
                "a": "Roz Shawarma is Sharief Bhai's sibling brand focused only on shawarma and rolls, "
                     "sharing kitchens but running a lighter, faster menu for quick-bite occasions.",
            },
        ],
    },
    {
        "slug": "olio",
        "name": "Olio",
        "full_name": "Olio",
        "category": "Pizza & Italian",
        "color": "#02311E",
        "logo": "/assets/images/logos/olio.png",
        "logo_bg": "#F9F1DD",
        "photo": "/assets/images/photos/olio-food.jpg",
        "domain": "https://www.oliopizza.in",
        "tagline": "Italian comfort food, kitchen-fresh.",
        "description": (
            "Olio serves Italian-inspired comfort food — pizza, pasta and sides — as one of "
            "Curefoods' core delivery brands, with a leaner spinoff, Enso, exploring a "
            "Japanese-fusion adjacent concept."
        ),
        "story": (
            "Olio focuses on the essentials of Italian comfort eating done consistently well: "
            "pizza and pasta cooked fresh per order rather than pre-batched. The brand's "
            "'core' menu is what most cities see; select clusters also run Enso, a related "
            "concept the team uses to test new formats."
        ),
        "menu": [
            {"veg": True, "name": "Alfredo Pasta", "detail": "Creamy white sauce pasta"},
            {"veg": True, "name": "Arrabbiata Penne", "detail": "Spicy tomato-basil pasta"},
            {"veg": True, "name": "Farmhouse Pizza", "detail": "Classic veg-loaded pizza"},
            {"veg": True, "name": "Garlic Bread Bites", "detail": "Side"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi", "Pune", "Kolkata", "Ahmedabad"],
        "store_count": "200+",
        "founded": "2021",
        "faq": [
            {
                "q": "What is Enso and how is it related to Olio?",
                "a": "Enso is a related, smaller-format concept run out of select Olio kitchens as Curefoods "
                     "tests new menu formats; it is not available in every city Olio serves.",
            }
        ],
    },
    {
        "slug": "arambam",
        "name": "Arambam",
        "full_name": "Arambam",
        "category": "Millet-first South Indian",
        "color": "#3E7A5C",
        "logo": "/assets/images/logos/arambam.webp",
        "photo": "/assets/images/photos/arambam-food.jpg",
        "domain": "https://www.arambam.com",
        "tagline": "5 states in 1 plate — wholesome South Indian, built on millets.",
        "description": (
            "Arambam is Curefoods' celebrity-backed South Indian brand, run out of its "
            "Millet Express subsidiary, serving comforting millet-forward regional dishes "
            "from across five South Indian states on one menu."
        ),
        "story": (
            "Arambam launched in partnership with actor Rakul Preet Singh, positioned around "
            "the nutritional case for millets over rice and wheat. Run by Curefoods' Millet "
            "Express subsidiary, it later entered an 18-month master franchise agreement with "
            "EAT360 to accelerate expansion beyond its Bengaluru and Mumbai launch markets."
        ),
        "menu": [
            {"veg": True, "name": "Ragi Mudde Combo", "detail": "Karnataka-style millet ball with sambar"},
            {"veg": True, "name": "Millet Bisi Bele Bath", "detail": "Millet-based one-pot rice"},
            {"veg": True, "name": "Andhra Millet Thali", "detail": "5-states-in-1-plate format"},
            {"veg": True, "name": "Jowar Dosa", "detail": "Multi-millet batter"},
        ],
        "cities": ["Bengaluru", "Mumbai", "Hyderabad"],
        "founded": "2024",
        "ambassador": "Rakul Preet Singh (brand partner)",
        "faq": [
            {
                "q": "What does '5 states in 1 plate' mean for Arambam?",
                "a": "It's Arambam's positioning line — a single menu spanning South Indian regional "
                     "styles across five states, built around millets instead of rice or wheat.",
            },
            {
                "q": "Is Arambam the same company as Millet Express?",
                "a": "Arambam is run by Curefoods' Millet Express subsidiary, which also operates the "
                     "separate Millet Express brand; the two share ownership but run distinct menus and storefronts.",
            },
        ],
    },
    {
        "slug": "krispy-kreme",
        "name": "Krispy Kreme",
        "full_name": "Krispy Kreme India",
        "category": "Doughnuts & Coffee (Global Partner Brand)",
        "color": "#00543D",
        "logo": "/assets/images/logos/krispy-kreme.png",
        "photo": "/assets/images/photos/krispy-kreme-food.jpg",
        "domain": "https://www.krispykremeindia.in",
        "tagline": "The world's doughnut, made fresh in India.",
        "description": (
            "Krispy Kreme is a global doughnut and coffee brand that Curefoods brought to "
            "India as master franchisee, running dine-in stores, kiosks and delivery under "
            "the international brand's own name and recipes."
        ),
        "story": (
            "Unlike Curefoods' home-grown brands, Krispy Kreme is an international master-"
            "franchise partnership — Curefoods operates the India business (stores, kitchens "
            "and delivery) under Krispy Kreme's global brand standards and recipes, betting "
            "that a globally trusted name accelerates trust and ticket size faster than a "
            "new brand could alone."
        ),
        "menu": [
            {"veg": True, "name": "Original Glazed Dozen", "detail": "The signature glazed doughnut"},
            {"veg": True, "name": "Chocolate Iced Kreme Filled", "detail": "Filled doughnut"},
            {"veg": True, "name": "Assorted Doughnut Box", "detail": "Mixed selection"},
            {"veg": True, "name": "Kreme Coffee", "detail": "Hot & cold coffee range"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Delhi NCR", "Jaipur", "Chandigarh"],
        "store_count": "150+",
        "founded": "2022 (Curefoods master franchise; global brand since 1937)",
        "faq": [
            {
                "q": "Is Krispy Kreme a Curefoods-owned brand or a franchise?",
                "a": "Krispy Kreme is a global brand; Curefoods operates it in India as master "
                     "franchisee, running local stores and delivery under Krispy Kreme's international "
                     "recipes and standards rather than owning the underlying IP.",
            },
        ],
    },
    {
        "slug": "nomad-pizza",
        "name": "Nomad Pizza",
        "full_name": "Nomad Pizza",
        "category": "Pizza",
        "color": "#A62639",
        "logo": "/assets/images/logos/nomad-pizza.png",
        "photo": "/assets/images/photos/nomad-pizza-food.jpg",
        "tagline": "Hand-stretched pizza, globally inspired.",
        "description": (
            "Nomad Pizza brings artisanal, hand-stretched pizzas with globally inspired "
            "toppings to Curefoods' delivery network, positioned as a premium everyday-pizza "
            "alternative to the big chains."
        ),
        "story": (
            "Nomad Pizza was built on a simple bet: Indian pizza delivery didn't need to mean "
            "assembly-line dough. Every base is hand-stretched to order, and the topping menu "
            "borrows from Nomad's travel-inspired name — Peri Peri, Korean BBQ, and classic "
            "Margherita sit on the same menu."
        ),
        "menu": [
            {"veg": True, "name": "Peri Peri Paneer Pizza", "detail": "Hand-stretched, wood-fired base"},
            {"veg": False, "name": "Korean BBQ Chicken Pizza", "detail": "Globally-inspired topping"},
            {"veg": True, "name": "Classic Margherita", "detail": "San Marzano-style tomato base"},
            {"veg": False, "name": "Nomad Meat Feast", "detail": "Four-meat loaded pizza"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Mumbai", "Delhi NCR"],
        "founded": "2021",
        "faq": [
            {
                "q": "What makes Nomad Pizza different from other pizza delivery brands?",
                "a": "Nomad Pizza hand-stretches every base to order and builds its menu around "
                     "globally-inspired toppings like Peri Peri and Korean BBQ alongside classics.",
            }
        ],
    },
    {
        "slug": "cakezone",
        "name": "CakeZone",
        "full_name": "CakeZone",
        "category": "Cakes & Celebrations",
        "color": "#C24E7B",
        "logo": "/assets/images/logos/cakezone.svg",
        "logo_bg": "#C24E7B",
        "photo": "/assets/images/photos/cakezone-food.jpg",
        "tagline": "Same-day cakes for every celebration.",
        "description": (
            "CakeZone is Curefoods' cakes and celebration-desserts brand, built around "
            "same-day and midnight delivery for birthdays, anniversaries and festive occasions."
        ),
        "story": (
            "CakeZone was brought into Curefoods to own the celebrations occasion — cakes, "
            "customised messages, and add-on gifting — with a delivery promise built around "
            "urgency: same-day and midnight slots for last-minute celebrations."
        ),
        "menu": [
            {"veg": True, "name": "Truffle Cake", "detail": "Half kg / 1 kg"},
            {"veg": True, "name": "Red Velvet Cake", "detail": "Half kg / 1 kg"},
            {"veg": True, "name": "Photo Cake", "detail": "Customisable"},
            {"veg": True, "name": "Pull-Me-Up Cake", "detail": "Layered surprise cake"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi NCR", "Pune", "Kolkata", "Ahmedabad", "Chandigarh", "Jaipur", "Coimbatore", "Indore"],
        "founded": "2020 (acquired by Curefoods)",
        "ambassador": "Nora Fatehi (brand ambassador & investor)",
        "faq": [
            {
                "q": "Does CakeZone deliver at midnight?",
                "a": "Yes — CakeZone offers midnight and same-day delivery slots designed for "
                     "last-minute birthday and anniversary celebrations.",
            }
        ],
    },
]

# Site-wide FAQ (in addition to per-brand FAQs), feeds the /faq.html hub — the
# single richest page for AEO / LLM citation.
SITE_FAQ = [
    {
        "q": "What is Curefoods?",
        "a": "Curefoods is a Bengaluru-headquartered house of food brands, founded in 2020 by "
             "Ankit Nagori. It builds and scales multiple F&B brands — spanning healthy meals, "
             "biryani, pizza, desserts and celebration cakes — out of a shared network of "
             "cloud kitchens and dine-in stores across India.",
    },
    {
        "q": "How many brands does Curefoods own?",
        "a": "Curefoods' published brand portfolio includes Kitchens of EatFit, Sharief Bhai, "
             "Olio Pizza, Arambam, Nomad Pizza, CakeZone and Frozen Bottle, plus master-franchise "
             "partner Krispy Kreme.",
    },
    {
        "q": "What is a 'house of brands' model, and why does Curefoods use it?",
        "a": "A house-of-brands model runs several distinct, independently-branded products from "
             "shared infrastructure — in Curefoods' case, shared cloud kitchens, supply chain and "
             "delivery operations. It lets one kitchen serve several occasions (health food, "
             "biryani, dessert) to the same customer without diluting any single brand's identity.",
    },
    {
        "q": "How many kitchens and stores does Curefoods operate?",
        "a": "As of March 31, 2025, Curefoods runs 281 cloud kitchens, 99 kiosks and 122 "
             "restaurants across India.",
    },
    {
        "q": "Who founded Curefoods and when?",
        "a": "Curefoods was founded in 2020 by Ankit Nagori, former co-founder of Cure.fit "
             "(Cult.fit) and former Chief Business Officer of Flipkart, who set out to apply the same operating rigor to "
             "the food-brands business.",
    },
    {
        "q": "How can I order from Curefoods brands?",
        "a": "Every Curefoods brand is listed on major food delivery platforms (Swiggy, Zomato) "
             "under its own name — search the brand name directly, e.g. 'EatFit' or 'Sharief "
             "Bhai' — and select brands also operate dedicated apps and dine-in stores.",
    },
    {
        "q": "Is Curefoods the same company as Rebel Foods?",
        "a": "No. Curefoods and Rebel Foods are separate, competing Indian cloud-kitchen "
             "companies that both use a house-of-brands model. Rebel Foods owns brands like "
             "Faasos, Behrouz Biryani and Oven Story; Curefoods owns EatFit, Sharief Bhai, "
             "CakeZone and the brands listed on this site.",
    },
    {
        "q": "Does Curefoods have physical, dine-in stores or only delivery kitchens?",
        "a": "Both. Most Curefoods brands operate delivery-only cloud kitchens, but several — "
             "including Sharief Bhai's Mosque Road flagship and Krispy Kreme's dine-in cafés — "
             "also run dine-in and walk-in retail formats.",
    },
    {
        "q": "How do I apply for a job at Curefoods?",
        "a": "Open roles across all Curefoods brands are listed on the Careers page "
             "(curefoods.in/careers.html); applications can also be sent to careers@curefoods.in.",
    },
    {
        "q": "How can franchise or partnership enquiries reach Curefoods?",
        "a": "Franchise and partnership enquiries can be sent to hello@curefoods.in.",
    },
]

VALUES = [
    {"title": "Kitchen-first economics", "text": "Every brand is designed around shared kitchen infrastructure, so unit economics work before marketing spend does."},
    {"title": "Category depth over breadth", "text": "Each brand owns one occasion — health, biryani, dessert, celebration — rather than trying to be everything to everyone."},
    {"title": "Data-run, fast to the door", "text": "Menu, pricing and kitchen placement are driven by order-level data, and kitchen density is built to shrink delivery time without shrinking food quality."},
]

CORE_PURPOSE = {
    "eyebrow": "Core Purpose",
    "title": "Create Iconic Food Brands",
    "paragraphs": [
        "Food is not just a necessity. It is a daily part of how people live, feel, and connect.",
        "Every meal is a moment.",
        "And over time, these moments build trust... and habit.",
        "At Curefoods, our role is not just to serve food, but to build brands that customers choose, remember, and come back to.",
        "We are here to create iconic food brands that customers remember, trust and love for years to come.",
    ],
}

CORE_VALUES = [
    {"title": "Love for Food", "icon": "/assets/images/values/value-love-for-food.png"},
    {"title": "Do More with Less", "icon": "/assets/images/values/value-do-more-with-less.png"},
    {"title": "Act Like an Owner", "icon": "/assets/images/values/value-act-like-owner.png"},
    {"title": "Pursuit of Excellence", "icon": "/assets/images/values/value-pursuit-excellence.png"},
]

# Pulled verbatim from curefoods.in/about ("We serve happiness to your plate
# across India" stats block) — not inferred or estimated.
FACILITY_STATS = {
    "as_of": "March 31, 2025",
    "items": [
        {"label": "Cloud Kitchens", "value": "281"},
        {"label": "Kiosks", "value": "99"},
        {"label": "Restaurants", "value": "122"},
    ],
}

# Real third-party press coverage — verified live before adding, not written by Curefoods.
NEWS_MENTIONS = [
    {
        "title": "Here's how Ankit Nagori plans to scale Curefoods",
        "source": "Business Today",
        "photo": "/assets/images/photos/curefoods-mascot.jpg",
        "url": "https://www.businesstoday.in/latest/corporate/story/heres-how-ankit-nagori-plans-to-scale-curefoods-526760-2026-04-21",
    },
    {
        "title": "Curefoods to unveil flagship Sharief Bhai Food Plaza in Bengaluru",
        "source": "Nuffoods Spectrum",
        "photo": "/assets/images/photos/sharief-bhai-store.jpg",
        "url": "https://nuffoodsspectrum.in/2025/06/02/curefoods-to-unveil-flagship-sharief-bhai-food-plaza-in-bengaluru.html",
    },
    {
        "title": "Sharief Bhai strengthens Bengaluru presence with multi-format food plaza",
        "source": "Restaurant India",
        "photo": "/assets/images/photos/sharief-bhai-store.jpg",
        "url": "https://www.restaurantindia.in/news/sharief-bhai-strengthens-bengaluru-presence-with-multi-format-food-plaza.n12901",
    },
    {
        "title": "Curefoods' subsidiary Millet Express enters master franchise agreement with EAT360 for Arambam",
        "source": "Restaurant India",
        "photo": "/assets/images/photos/arambam-food.jpg",
        "url": "https://www.restaurantindia.in/news/curefoods-signs-18-month-franchise-agreement-with-eat360-for-arambam-brand.n12946",
    },
    {
        "title": "Curefoods backs millet-based food brand Millet Express",
        "source": "Entrackr",
        "photo": "/assets/images/photos/arambam-food.jpg",
        "url": "https://entrackr.com/2023/07/curefoods-backs-millet-based-food-brand-millet-express/",
    },
    {
        "title": "Ankit Nagori, CEO of Curefoods, on building India's cloud kitchen empire",
        "source": "Franchise India",
        "photo": "/assets/images/photos/india-map.png",
        "url": "https://www.franchiseindia.com/insights/en/interview/ankit-nagori-ceo-of-curefoods-on-building-indias-cloud-kitchen-empire.57613",
    },
]
