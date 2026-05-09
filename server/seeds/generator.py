import random
from faker import Faker
from datetime import datetime, timezone

fake = Faker()
_SEED = 42
fake.seed_instance(_SEED)
random.seed(_SEED)


def random_price(min_p: float, max_p: float, round_to: int = 2) -> float:
    return round(random.uniform(min_p, max_p), round_to)


def random_specs(base_specs: dict) -> dict:
    return {k: v for k, v in base_specs.items()}


def fake_description(name: str, brand: str, category: str) -> str:
    templates = [
        f"High-performance {name} from {brand}. Engineered for demanding {category} workloads with cutting-edge technology and premium build quality.",
        f"Experience next-level performance with the {brand} {name}. Optimized for gaming, content creation, and professional applications.",
        f"The {brand} {name} delivers exceptional {category.lower()} performance. Features advanced thermal design and robust construction.",
        f"Elevate your build with the {brand} {name}. Built for enthusiasts who demand the best in {category.lower()} technology.",
    ]
    return random.choice(templates)


def fake_review(name: str) -> str:
    reviews = [
        f"Absolutely incredible performance. The {name} exceeded all my expectations.",
        f"Great value for the price. Would definitely recommend to anyone building a new PC.",
        f"Solid build quality and excellent thermal performance. Very satisfied with this purchase.",
        f"Perfect for my build. Installation was straightforward and it works flawlessly.",
        f"Top-tier performance. This {name} is a beast and handles everything I throw at it.",
    ]
    return random.choice(reviews)


def generate_product_variations(base_name: str, brand: str, category: str, count: int = 3) -> list[dict]:
    """Generate fake product variations for categories without specific data"""
    variants = []
    suffixes = ["Pro", "Elite", "Max", "Ultra", "Prime", "Plus", "Premium", "Slim", "V2", "Gen 2"]
    for i in range(count):
        suffix = random.choice(suffixes)
        variants.append({
            "name": f"{base_name} {suffix}",
            "brand": brand,
            "category": category,
            "manufacturer": brand,
            "model": f"{base_name.replace(' ', '')}{suffix}",
            "price": random_price(29.99, 299.99),
            "power_consumption": random.randint(5, 150),
            "specs": {"variant": suffix, "color": random.choice(["Black", "White", "RGB"]), "material": random.choice(["Aluminum", "Steel", "Plastic", "Carbon Fiber"])},
            "compatibility": {"universal": True},
        })
    return variants


def generate_fake_user() -> dict:
    """Generate a random user profile"""
    username = fake.user_name()
    return {
        "username": username,
        "email": f"{username.lower()}@xp.game",
        "bio": fake.text(max_nb_chars=120),
        "location": f"{fake.city()}, {fake.country()}",
        "xp": random.randint(100, 10000),
    }
