DEFAULT_RESTAURANTS = [
    {
        "name": "Udupi Garden",
        "description": "Delicious South Indian cuisine served fresh for family-style dining.",
        "location": "Bengaluru",
        "cuisine": "South Indian",
    },
    {
        "name": "Soofi Mandi",
        "description": "Fragrant rice, tender chicken, and generous platters for groups.",
        "location": "Bengaluru",
        "cuisine": "Mandi",
    },
    {
        "name": "Rameshwaram Cafe",
        "description": "Sumptuous South Indian breakfast classics with quick service.",
        "location": "Bengaluru",
        "cuisine": "Breakfast",
    },
    {
        "name": "Onesta",
        "description": "The city's relaxed pizza table for slices, celebrations, and friends.",
        "location": "Bengaluru",
        "cuisine": "Pizza",
    },
]

DEFAULT_CHEFS = [
    {
        "name": "Chef Sanjeev Kapoor",
        "signature_dish": "Shaam Savera",
        "cuisine": "Italian",
        "contact": "9876543210",
        "email": "sanjeev@example.com",
        "bio": "Known for elegant private dining menus and memorable signature dishes.",
    },
    {
        "name": "Chef Venkatesh Bhatt",
        "signature_dish": "Poondu kuzhambu",
        "cuisine": "South Indian",
        "contact": "9876543211",
        "email": "venkatesh@example.com",
        "bio": "A South Indian specialist for festive meals, family dinners, and classic flavors.",
    },
    {
        "name": "Chef Ranveer Brar",
        "signature_dish": "Dorra Kebab",
        "cuisine": "Seafood",
        "contact": "9876543212",
        "email": "ranveer@example.com",
        "bio": "Creates rich, story-led menus with bold spices and polished presentation.",
    },
    {
        "name": "Chef Koushik S. A.K.A.",
        "signature_dish": "Paneer tikka pizza",
        "cuisine": "Pan-Asian",
        "contact": "9876543213",
        "email": "koushik@example.com",
        "bio": "A playful private chef for fusion menus, parties, and relaxed celebrations.",
    },
]


def ensure_default_content():
    from .models import Chef, Restaurant

    if not Restaurant.objects.exists():
        Restaurant.objects.bulk_create(
            Restaurant(image="", **restaurant)
            for restaurant in DEFAULT_RESTAURANTS
        )

    if not Chef.objects.exists():
        Chef.objects.bulk_create(
            Chef(image="", **chef)
            for chef in DEFAULT_CHEFS
        )
