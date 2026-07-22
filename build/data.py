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
        "Curefoods is India's leading house of food brands, building and scaling "
        "category-defining F&B brands — from healthy meals to biryani, pizza to "
        "desserts — out of 400+ kitchens and stores across 60+ cities."
    ),
    "founder": "Ankit Nagori",
    "founded_year": "2020",
    "hq": "Bengaluru, Karnataka, India",
    "stats": [
        {"value": "15+", "label": "Brands under one roof"},
        {"value": "400+", "label": "Kitchens & stores"},
        {"value": "60+", "label": "Cities served"},
        {"value": "₹1,420 Cr", "label": "FY24 revenue"},
    ],
    "social": {
        "instagram": "https://www.instagram.com/curefoods.in/",
        "linkedin": "https://in.linkedin.com/company/curefoods",
        "twitter": "https://twitter.com/curefoods_in",
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
    {"label": "Investors", "href": "/investors.html"},
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
        "emoji": "🥗",
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
            {"name": "Peri Peri Chicken Rice Bowl", "detail": "420 kcal · 32g protein"},
            {"name": "Paneer Tikka Overload Bowl", "detail": "390 kcal · 24g protein"},
            {"name": "Grilled Chicken Salad", "detail": "310 kcal · 28g protein"},
            {"name": "Quinoa Khichdi", "detail": "340 kcal · 14g protein"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi NCR", "Pune"],
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
                "a": "EatFit operates in Bengaluru, Hyderabad, Chennai, Mumbai, Delhi NCR and Pune, with kitchens "
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
        "emoji": "🍛",
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
            {"name": "Hyderabadi Chicken Dum Biryani", "detail": "Signature slow-dum biryani"},
            {"name": "Chicken Mandi", "detail": "Arabian-style rice & smoked chicken"},
            {"name": "Ghee Rice Combo", "detail": "Multiple ghee rice variants"},
            {"name": "Seekh Kebab Platter", "detail": "Char-grilled kebabs"},
        ],
        "cities": ["Bengaluru", "Chennai", "Coimbatore", "Mysuru"],
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
                "a": "Sharief Bhai operates across Karnataka and Tamil Nadu clusters; it does not currently "
                     "have stores in Hyderabad or the rest of Telangana.",
            },
            {
                "q": "What is the difference between Sharief Bhai and Roz Shawarma?",
                "a": "Roz Shawarma is Sharief Bhai's sibling brand focused only on shawarma and rolls, "
                     "sharing kitchens but running a lighter, faster menu for quick-bite occasions.",
            },
        ],
    },
    {
        "slug": "roz-shawarma",
        "name": "Roz Shawarma",
        "full_name": "Roz Shawarma",
        "category": "Shawarma & Rolls",
        "color": "#C4581B",
        "emoji": "🌯",
        "tagline": "Everyday shawarma, rolled fresh.",
        "description": (
            "Roz Shawarma is Curefoods' quick-bite shawarma and rolls brand, born out of "
            "Sharief Bhai's kitchens to serve a faster, everyday occasion at a lower ticket size."
        ),
        "story": (
            "'Roz' means 'everyday' — and that's the brief: a shawarma good enough to order "
            "daily, at a price and speed that supports it. Roz Shawarma shares kitchen "
            "infrastructure with Sharief Bhai across Karnataka and Tamil Nadu, letting Curefoods "
            "serve two very different occasions — a full biryani meal versus a quick roll — "
            "from the same four walls."
        ),
        "menu": [
            {"name": "Classic Chicken Shawarma Roll", "detail": "House garlic mayo"},
            {"name": "Paneer Shawarma Roll", "detail": "Vegetarian option"},
            {"name": "Shawarma Rice Bowl", "detail": "Shawarma over spiced rice"},
            {"name": "Loaded Fries", "detail": "Shawarma-topped fries"},
        ],
        "cities": ["Bengaluru", "Chennai", "Coimbatore"],
        "founded": "2022",
        "faq": [
            {
                "q": "Is Roz Shawarma a separate app from Sharief Bhai?",
                "a": "Roz Shawarma is ordered through the same Curefoods brand network as Sharief Bhai and is "
                     "listed on major food delivery platforms as its own storefront.",
            },
            {
                "q": "Does Roz Shawarma serve Hyderabad?",
                "a": "No — like Sharief Bhai, Roz Shawarma currently operates only in Karnataka and Tamil Nadu, "
                     "with no stores in Hyderabad or Telangana.",
            },
        ],
    },
    {
        "slug": "nomad-pizza",
        "name": "Nomad Pizza",
        "full_name": "Nomad Pizza",
        "category": "Pizza",
        "color": "#A62639",
        "emoji": "🍕",
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
            {"name": "Peri Peri Paneer Pizza", "detail": "Hand-stretched, wood-fired base"},
            {"name": "Korean BBQ Chicken Pizza", "detail": "Globally-inspired topping"},
            {"name": "Classic Margherita", "detail": "San Marzano-style tomato base"},
            {"name": "Nomad Meat Feast", "detail": "Four-meat loaded pizza"},
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
        "slug": "frozen-bottle",
        "name": "Frozen Bottle",
        "full_name": "Frozen Bottle",
        "category": "Shakes & Desserts",
        "color": "#2C6E8E",
        "emoji": "🥤",
        "domain": "https://www.frozenbottle.com",
        "tagline": "Thick shakes, waffles and dessert-in-a-bottle.",
        "description": (
            "Frozen Bottle specialises in indulgent thick shakes, waffles and jar desserts, "
            "acquired into the Curefoods portfolio to round out its dessert and beverages layer."
        ),
        "story": (
            "Frozen Bottle joined Curefoods as part of its dessert and beverages expansion, "
            "bringing a cult following for its bottle-served thick shakes. The brand runs both "
            "dine-in kiosks in malls and high streets, and delivery-only listings, making it one "
            "of the few Curefoods brands with a strong offline retail footprint."
        ),
        "menu": [
            {"name": "Oreo Overload Shake", "detail": "Signature thick shake"},
            {"name": "Nutella Waffle", "detail": "Belgian waffle, warm Nutella"},
            {"name": "Biscoff Jar", "detail": "Layered jar dessert"},
            {"name": "Cold Coffee Frappe", "detail": "House blend"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Pune", "Delhi NCR", "Mumbai"],
        "founded": "2016 (acquired by Curefoods 2021)",
        "faq": [
            {
                "q": "Does Frozen Bottle have physical stores or only delivery?",
                "a": "Frozen Bottle runs both dine-in kiosks in malls and high streets as well as "
                     "delivery-only listings on food aggregator apps.",
            }
        ],
    },
    {
        "slug": "olio",
        "name": "Olio",
        "full_name": "Olio",
        "category": "Pizza & Italian",
        "color": "#7A5C2E",
        "emoji": "🍝",
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
            {"name": "Alfredo Pasta", "detail": "Creamy white sauce pasta"},
            {"name": "Arrabbiata Penne", "detail": "Spicy tomato-basil pasta"},
            {"name": "Farmhouse Pizza", "detail": "Classic veg-loaded pizza"},
            {"name": "Garlic Bread Bites", "detail": "Side"},
        ],
        "cities": ["Bengaluru", "Chennai", "Hyderabad"],
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
        "slug": "cakezone",
        "name": "CakeZone",
        "full_name": "CakeZone",
        "category": "Cakes & Celebrations",
        "color": "#C24E7B",
        "emoji": "🎂",
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
            {"name": "Truffle Cake", "detail": "Half kg / 1 kg"},
            {"name": "Red Velvet Cake", "detail": "Half kg / 1 kg"},
            {"name": "Photo Cake", "detail": "Customisable"},
            {"name": "Pull-Me-Up Cake", "detail": "Layered surprise cake"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi NCR", "Pune", "Kolkata"],
        "founded": "2020 (acquired by Curefoods)",
        "faq": [
            {
                "q": "Does CakeZone deliver at midnight?",
                "a": "Yes — CakeZone offers midnight and same-day delivery slots designed for "
                     "last-minute birthday and anniversary celebrations.",
            }
        ],
    },
    {
        "slug": "rolls-on-wheels",
        "name": "Rolls on Wheels",
        "full_name": "Rolls on Wheels",
        "category": "Rolls & Wraps",
        "color": "#8C3B2E",
        "emoji": "🌮",
        "tagline": "Kathi rolls, kept simple.",
        "description": (
            "Rolls on Wheels is a Kitchens-of-EatFit sister brand serving Kolkata-style kathi "
            "rolls and wraps as a quick, affordable everyday meal."
        ),
        "story": (
            "Part of the Kitchens of EatFit shared-kitchen family, Rolls on Wheels keeps the "
            "menu tight and the format street-food-authentic — parathas rolled fresh with "
            "kebabs, eggs or paneer, built for a fast, low-ticket order that pairs well with "
            "other EatFit-family dishes in the same basket."
        ),
        "menu": [
            {"name": "Chicken Kathi Roll", "detail": "Classic Kolkata-style"},
            {"name": "Egg Roll", "detail": "Double-egg option"},
            {"name": "Paneer Tikka Roll", "detail": "Vegetarian"},
            {"name": "Mutton Seekh Roll", "detail": "Premium option"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai"],
        "founded": "2022",
        "faq": [],
    },
    {
        "slug": "great-indian-khichdi",
        "name": "Great Indian Khichdi",
        "full_name": "Great Indian Khichdi (GIK)",
        "category": "Comfort Meals",
        "color": "#5B7B3A",
        "emoji": "🍚",
        "tagline": "Khichdi, reinvented for every craving.",
        "description": (
            "Great Indian Khichdi turns India's ultimate comfort food into a full menu of "
            "flavoured khichdis, positioned as a lighter, home-style alternative within the "
            "Kitchens of EatFit family."
        ),
        "story": (
            "Great Indian Khichdi exists to prove that comfort food and convenience aren't "
            "opposites — a rotating menu of khichdi variants, from classic moong dal to loaded "
            "vegetable and protein versions, cooked fresh in the same shared kitchens as EatFit."
        ),
        "menu": [
            {"name": "Classic Moong Dal Khichdi", "detail": "Home-style"},
            {"name": "Vegetable Loaded Khichdi", "detail": "Extra veggies"},
            {"name": "Paneer Khichdi", "detail": "Protein-rich"},
            {"name": "Kadhi Khichdi Combo", "detail": "With kadhi"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai"],
        "founded": "2021",
        "faq": [],
    },
    {
        "slug": "homeplate",
        "name": "Homeplate",
        "full_name": "Homeplate",
        "category": "Home-style Meals",
        "color": "#9C6B30",
        "emoji": "🍱",
        "tagline": "Thalis and home-style meals, delivered.",
        "description": (
            "Homeplate serves regional Indian thalis and home-style meal combos, part of the "
            "Kitchens of EatFit family, for customers who want a full home-cooked-style meal "
            "without home-cooking."
        ),
        "story": (
            "Homeplate's menu rotates regional thalis — North Indian, South Indian and combo "
            "meal formats — cooked in the same kitchens as EatFit and its sister brands, "
            "designed for the daily-lunch and family-dinner occasion."
        ),
        "menu": [
            {"name": "North Indian Thali", "detail": "Dal, sabzi, roti, rice"},
            {"name": "South Indian Meal", "detail": "Sambar, rasam, rice, curry"},
            {"name": "Rajma Chawal Combo", "detail": "Home-style combo"},
            {"name": "Chole Bhature", "detail": "Weekend special"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai"],
        "founded": "2021",
        "faq": [],
    },
    {
        "slug": "chaat-street",
        "name": "Chaat Street",
        "full_name": "Chaat Street",
        "category": "Street Food",
        "color": "#D6672A",
        "emoji": "🥙",
        "tagline": "Street-side chaat, cloud-kitchen fresh.",
        "description": (
            "Chaat Street brings India's street-food chaat culture — pani puri, bhel, "
            "aloo tikki — to delivery, as part of the Kitchens of EatFit family."
        ),
        "story": (
            "Chaat is notoriously hard to deliver well — Chaat Street's entire product design "
            "is built around packaging that keeps crunch separate from chutney until the last "
            "moment, so the chaat still tastes street-fresh at the door."
        ),
        "menu": [
            {"name": "Dahi Puri", "detail": "Assemble-at-home packaging"},
            {"name": "Ragda Pattice", "detail": "Mumbai-style"},
            {"name": "Bhel Puri", "detail": "Classic"},
            {"name": "Aloo Tikki Chaat", "detail": "With sev & chutneys"},
        ],
        "cities": ["Bengaluru", "Hyderabad"],
        "founded": "2022",
        "faq": [],
    },
    {
        "slug": "millet-express",
        "name": "Millet Express",
        "full_name": "Millet Express",
        "category": "Millet Bowls",
        "color": "#8A9A3E",
        "emoji": "🌾",
        "tagline": "Millet-first bowls for the health-conscious.",
        "description": (
            "Millet Express builds its entire menu around millets — ragi, jowar, bajra — as a "
            "climate-friendly, high-fibre alternative to rice and wheat, within the Kitchens "
            "of EatFit family."
        ),
        "story": (
            "Riding India's millet resurgence, Millet Express replaces rice and wheat with "
            "ragi, jowar and bajra across its bowls, dosas and khichdis — sharing kitchens "
            "with Madras Curd Rice Company and the rest of the EatFit family."
        ),
        "menu": [
            {"name": "Ragi Veg Bowl", "detail": "Millet-based bowl"},
            {"name": "Jowar Roti Combo", "detail": "With sabzi & dal"},
            {"name": "Bajra Khichdi", "detail": "High-fibre"},
            {"name": "Millet Dosa", "detail": "Multi-millet batter"},
        ],
        "cities": ["Bengaluru", "Chennai"],
        "founded": "2023",
        "faq": [],
    },
    {
        "slug": "madras-curd-rice-company",
        "name": "Madras Curd Rice Company",
        "full_name": "Madras Curd Rice Company (MCRC)",
        "category": "South Indian",
        "color": "#3E6B6B",
        "emoji": "🍚",
        "tagline": "Curd rice, the way Chennai makes it.",
        "description": (
            "Madras Curd Rice Company is a hyper-focused South Indian brand built around "
            "curd rice and traditional accompaniments, part of the Kitchens of EatFit family "
            "and strongest in Chennai and Tamil Nadu."
        ),
        "story": (
            "MCRC bets on doing one dish exceptionally well: Madras-style curd rice, "
            "tempered and served with authentic sides like mor milagai and pickle, for the "
            "light-meal and end-of-day comfort-food occasion."
        ),
        "menu": [
            {"name": "Classic Curd Rice", "detail": "Tempered, with pickle"},
            {"name": "Curd Rice + Vathal Combo", "detail": "With mor milagai"},
            {"name": "Lemon Rice Combo", "detail": "Side option"},
            {"name": "Sambar Rice Combo", "detail": "Side option"},
        ],
        "cities": ["Chennai", "Bengaluru"],
        "founded": "2023",
        "faq": [],
    },
    {
        "slug": "arambam",
        "name": "Arambam",
        "full_name": "Arambam",
        "category": "Millet-first South Indian",
        "color": "#3E7A5C",
        "emoji": "🍲",
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
            {"name": "Ragi Mudde Combo", "detail": "Karnataka-style millet ball with sambar"},
            {"name": "Millet Bisi Bele Bath", "detail": "Millet-based one-pot rice"},
            {"name": "Andhra Millet Thali", "detail": "5-states-in-1-plate format"},
            {"name": "Jowar Dosa", "detail": "Multi-millet batter"},
        ],
        "cities": ["Bengaluru", "Mumbai"],
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
        "emoji": "🍩",
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
            {"name": "Original Glazed Dozen", "detail": "The signature glazed doughnut"},
            {"name": "Chocolate Iced Kreme Filled", "detail": "Filled doughnut"},
            {"name": "Assorted Doughnut Box", "detail": "Mixed selection"},
            {"name": "Kreme Coffee", "detail": "Hot & cold coffee range"},
        ],
        "cities": ["Bengaluru", "Mumbai", "Delhi NCR", "Hyderabad", "Pune"],
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
        "a": "Curefoods operates 15+ brands, including EatFit, Sharief Bhai, Roz Shawarma, Nomad "
             "Pizza, Frozen Bottle, Olio, CakeZone, Arambam, the Kitchens-of-EatFit family "
             "(Rolls on Wheels, Great Indian Khichdi, Homeplate, Chaat Street, Millet Express, "
             "Madras Curd Rice Company), and master-franchise partner Krispy Kreme.",
    },
    {
        "q": "What is a 'house of brands' model, and why does Curefoods use it?",
        "a": "A house-of-brands model runs several distinct, independently-branded products from "
             "shared infrastructure — in Curefoods' case, shared cloud kitchens, supply chain and "
             "delivery operations. It lets one kitchen serve several occasions (health food, "
             "biryani, dessert) to the same customer without diluting any single brand's identity.",
    },
    {
        "q": "How many cities and kitchens does Curefoods operate?",
        "a": "As of its latest reported figures, Curefoods runs 400+ kitchens and stores across "
             "60+ cities in India, with select brands also present internationally.",
    },
    {
        "q": "Who founded Curefoods and when?",
        "a": "Curefoods was founded in 2020 by Ankit Nagori, former co-founder and Chief Business "
             "Officer of Cure.fit (Cult.fit), who set out to apply the same operating rigor to "
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
             "including Sharief Bhai's Mosque Road flagship and Frozen Bottle's mall kiosks — "
             "also run dine-in and walk-in retail formats.",
    },
    {
        "q": "How do I apply for a job at Curefoods?",
        "a": "Open roles across all Curefoods brands are listed on the Careers page "
             "(curefoods.in/careers.html); applications can also be sent to careers@curefoods.in.",
    },
    {
        "q": "How can investors or franchise partners contact Curefoods?",
        "a": "Investor relations and partnership enquiries can be made via the Investors page "
             "(curefoods.in/investors.html) or by writing to hello@curefoods.in.",
    },
]

VALUES = [
    {"title": "Kitchen-first economics", "text": "Every brand is designed around shared kitchen infrastructure, so unit economics work before marketing spend does."},
    {"title": "Category depth over breadth", "text": "Each brand owns one occasion — health, biryani, dessert, celebration — rather than trying to be everything to everyone."},
    {"title": "Data-run operations", "text": "Menu, pricing and kitchen placement decisions are driven by order-level data across every brand and city."},
    {"title": "Speed to the door", "text": "Kitchen density and route optimisation are built to shrink delivery time without shrinking food quality."},
]

TIMELINE = [
    {"year": "2020", "text": "Curefoods founded by Ankit Nagori; EatFit launches as the flagship brand."},
    {"year": "2021", "text": "Portfolio expands rapidly — Sharief Bhai, Nomad Pizza, Olio, Frozen Bottle and CakeZone join or launch."},
    {"year": "2022", "text": "Roz Shawarma, Rolls on Wheels and Chaat Street launch; Curefoods signs on as Krispy Kreme's India master franchisee; Kitchens of EatFit shared-kitchen model takes shape."},
    {"year": "2023", "text": "'Kitchens of EatFit' formally launches with Hrithik Roshan as brand ambassador and investor; Millet Express and Madras Curd Rice Company join."},
    {"year": "2024", "text": "Curefoods crosses ₹1,420 Cr in FY24 revenue, operating 400+ kitchens and stores across 60+ cities; Arambam launches with Rakul Preet Singh."},
]
