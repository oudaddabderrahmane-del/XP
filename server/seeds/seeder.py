import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from config.database import SessionLocal, init_db
from models.models import Category, Subcategory, PCPart, User, Community, Product
from utils.auth import hash_password
from seeds.data import CATEGORIES, SUBCATEGORIES, PRODUCTS
from seeds.catalog import generate_all_catalog
from seeds.generator import fake_description, random_price


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-").replace("/", "-").replace("&", "and").replace("--", "-").strip("-")


class SeedEngine:
    def __init__(self, db: Session):
        self.db = db
        self.stats = {"categories": 0, "subcategories": 0, "products": 0, "users": 0, "communities": 0, "marketplace_products": 0}
        self._category_cache: dict[str, Category] = {}
        self._subcategory_cache: dict[str, Subcategory] = {}

    # ---------- Duplicate Prevention ----------

    def _exists_cat(self, slug: str) -> bool:
        return self.db.query(Category).filter(Category.slug == slug).first() is not None

    def _exists_subcat(self, slug: str) -> bool:
        return self.db.query(Subcategory).filter(Subcategory.slug == slug).first() is not None

    def _exists_part(self, name: str) -> bool:
        return self.db.query(PCPart).filter(PCPart.name == name).first() is not None

    def _exists_user(self, email: str) -> bool:
        return self.db.query(User).filter(User.email == email).first() is not None

    def _exists_community(self, name: str) -> bool:
        return self.db.query(Community).filter(Community.name == name).first() is not None

    def _exists_marketplace_product(self, title: str) -> bool:
        return self.db.query(Product).filter(Product.title == title).first() is not None

    # ---------- Category Seeder ----------

    def seed_categories(self):
        count = 0
        for cat in CATEGORIES:
            if self._exists_cat(cat["slug"]):
                continue
            c = Category(
                id=str(uuid.uuid4()),
                name=cat["name"],
                slug=cat["slug"],
                icon=cat.get("icon"),
                description=cat.get("description", f"Browse {cat['name']} on XP"),
                sort_order=cat.get("sort_order", 0),
            )
            self.db.add(c)
            self._category_cache[cat["slug"]] = c
            count += 1
        if count:
            self.db.flush()
            for cat in CATEGORIES:
                if cat["slug"] not in self._category_cache:
                    existing = self.db.query(Category).filter(Category.slug == cat["slug"]).first()
                    if existing:
                        self._category_cache[cat["slug"]] = existing
        self.stats["categories"] += count
        return count

    # ---------- Subcategory Seeder ----------

    def seed_subcategories(self):
        self.seed_categories()
        count = 0
        for cat_slug, subs in SUBCATEGORIES.items():
            cat = self._category_cache.get(cat_slug) or self.db.query(Category).filter(Category.slug == cat_slug).first()
            if not cat:
                continue
            for sub in subs:
                if self._exists_subcat(sub["slug"]):
                    continue
                s = Subcategory(
                    id=str(uuid.uuid4()),
                    name=sub["name"],
                    slug=sub["slug"],
                    category_id=cat.id,
                    description=sub.get("description", f"{sub['name']} - {cat.name}"),
                    sort_order=sub.get("sort_order", 0),
                )
                self.db.add(s)
                self._subcategory_cache[sub["slug"]] = s
                count += 1
        if count:
            self.db.flush()
            for cat_slug, subs in SUBCATEGORIES.items():
                for sub in subs:
                    if sub["slug"] not in self._subcategory_cache:
                        existing = self.db.query(Subcategory).filter(Subcategory.slug == sub["slug"]).first()
                        if existing:
                            self._subcategory_cache[sub["slug"]] = existing
        self.stats["subcategories"] += count
        return count

    # ---------- Product Seeder ----------

    def seed_products(self):
        self.seed_subcategories()
        count = 0
        for p in PRODUCTS:
            if self._exists_part(p["name"]):
                continue
            subcat = self._subcategory_cache.get(p.get("subcategory_slug", ""))
            cat = None
            if subcat:
                cat = self.db.query(Category).filter(Category.id == subcat.category_id).first()

            part = PCPart(
                id=str(uuid.uuid4()),
                name=p["name"],
                brand=p.get("brand", ""),
                category=p["category"],
                category_id=cat.id if cat else None,
                subcategory_id=subcat.id if subcat else None,
                manufacturer=p.get("manufacturer", "Unknown"),
                model=p.get("model", p["name"]),
                specs=p.get("specs", {}),
                price=p["price"],
                power_consumption=p.get("power_consumption"),
                compatibility=p.get("compatibility", {}),
                image_url=f"/images/parts/{slugify(p['name'])}.jpg",
                stock_status= "in_stock",
                is_active=True,
            )
            self.db.add(part)
            count += 1
        self.db.flush()
        self.stats["products"] += count
        return count

    # ---------- Catalog Generator ----------

    def seed_catalog(self):
        self.seed_subcategories()
        generated = generate_all_catalog()
        count = 0
        for p in generated:
            if self._exists_part(p["name"]):
                continue
            subcat = self._subcategory_cache.get(p.get("subcategory_slug", ""))
            cat = None
            if subcat:
                cat = self.db.query(Category).filter(Category.id == subcat.category_id).first()
            part = PCPart(
                id=str(uuid.uuid4()),
                name=p["name"],
                brand=p.get("brand", ""),
                category=p["category"],
                category_id=cat.id if cat else None,
                subcategory_id=subcat.id if subcat else None,
                manufacturer=p.get("manufacturer", "Unknown"),
                model=p.get("model", p["name"]),
                specs=p.get("specs", {}),
                price=p["price"],
                power_consumption=p.get("power_consumption"),
                compatibility=p.get("compatibility", {}),
                image_url=f"/images/parts/{slugify(p['name'])}.jpg",
                stock_status="in_stock",
                is_active=True,
            )
            self.db.add(part)
            count += 1
        self.db.flush()
        self.stats["products"] += count
        return count

    # ---------- User Seeder ----------

    def seed_users(self):
        users_data = [
            {"username": "admin", "email": "admin@xp.game", "password": "admin123", "xp": 9999, "level": 50, "role": "admin", "bio": "XP Platform Administrator", "location": "Cyber City"},
            {"username": "gamer1", "email": "gamer@xp.game", "password": "password123", "xp": 500, "level": 10, "role": "user", "bio": "Casual gamer and tech enthusiast", "location": "Los Angeles, CA"},
            {"username": "techdev", "email": "dev@xp.game", "password": "dev123", "xp": 1200, "level": 20, "role": "user", "bio": "Full-stack developer & hardware geek", "location": "Seattle, WA"},
            {"username": "PixelMaster", "email": "pixel@xp.game", "password": "password123", "xp": 7500, "level": 35, "role": "moderator", "bio": "PC building enthusiast & photographer", "location": "New York, NY"},
            {"username": "CodeWizard", "email": "wizard@xp.game", "password": "password123", "xp": 6200, "level": 30, "role": "user", "bio": "Full-stack dev & gaming hardware collector", "location": "Austin, TX"},
            {"username": "NeonRider", "email": "neon@xp.game", "password": "password123", "xp": 4800, "level": 25, "role": "user", "bio": "RGB everything | Cyberpunk lover", "location": "Tokyo, Japan"},
            {"username": "BuildMaster", "email": "build@xp.game", "password": "password123", "xp": 3500, "level": 22, "role": "verified_seller", "bio": "Custom PC builder since 2018", "location": "London, UK"},
            {"username": "EliteGamer", "email": "elite@xp.game", "password": "password123", "xp": 2800, "level": 18, "role": "user", "bio": "Competitive FPS gamer & streamer", "location": "Berlin, Germany"},
            {"username": "DataStream", "email": "data@xp.game", "password": "password123", "xp": 1900, "level": 15, "role": "user", "bio": "AI/ML engineer exploring hardware", "location": "San Francisco, CA"},
            {"username": "CryptoVault", "email": "crypto@xp.game", "password": "password123", "xp": 1500, "level": 13, "role": "verified_seller", "bio": "Hardware trader & crypto enthusiast", "location": "Miami, FL"},
        ]
        count = 0
        for u in users_data:
            if self._exists_user(u["email"]):
                continue
            level = u.get("level", 1)
            user = User(
                id=str(uuid.uuid4()),
                username=u["username"],
                email=u["email"],
                hashed_password=hash_password(u["password"]),
                bio=u.get("bio", ""),
                location=u.get("location", ""),
                xp=u["xp"],
                level=level,
                role=u.get("role", "user"),
                is_verified=u.get("is_verified", False),
                badges=u.get("badges", []),
            )
            self.db.add(user)
            count += 1
        self.db.flush()
        self.stats["users"] += count
        return count

    # ---------- Community Seeder ----------

    def seed_communities(self):
        admin = self.db.query(User).filter(User.email == "admin@xp.game").first()
        gamer = self.db.query(User).filter(User.email == "gamer@xp.game").first()
        if not admin:
            return 0
        communities = [
            {"name": "PC Builders", "description": "Share and discuss PC builds, ask for advice, and show off your rig", "owner_id": admin.id},
            {"name": "Gaming", "description": "Everything gaming - discussions, reviews, and multiplayer sessions", "owner_id": admin.id},
            {"name": "Developers", "description": "For devs and programmers to discuss code, tools, and tech", "owner_id": admin.id},
            {"name": "AI & Tech", "description": "AI discussions, ML models, and cutting-edge tech news", "owner_id": gamer.id if gamer else admin.id},
        ]
        count = 0
        for c in communities:
            if self._exists_community(c["name"]):
                continue
            community = Community(id=str(uuid.uuid4()), **c)
            self.db.add(community)
            count += 1
        self.db.flush()
        self.stats["communities"] += count
        return count

    # ---------- Marketplace Product Seeder ----------

    def seed_marketplace_products(self):
        seller = self.db.query(User).filter(User.email == "gamer@xp.game").first()
        admin = self.db.query(User).filter(User.email == "admin@xp.game").first()
        if not seller or not admin:
            return 0
        products = [
            {"title": "RTX 4090 Gaming OC", "price": 1599.99, "category": "GPU", "condition": "new", "seller_id": seller.id, "location": "New York, NY"},
            {"title": "PlayStation 5 Digital Edition", "price": 399.99, "category": "Console", "condition": "used", "seller_id": seller.id, "location": "Los Angeles, CA"},
            {"title": "Gaming PC RTX 4070 + i7", "price": 1299.99, "category": "PC", "condition": "new", "seller_id": seller.id, "location": "Austin, TX"},
            {"title": "Intel Core i7-13700K (New)", "price": 449.99, "category": "CPU", "condition": "new", "seller_id": admin.id, "location": "Seattle, WA"},
            {"title": "Corsair 32GB DDR5 RAM Kit", "price": 109.99, "category": "RAM", "condition": "new", "seller_id": admin.id, "location": "Miami, FL"},
            {"title": "ASUS ROG Strix RTX 4070 Ti", "price": 849.99, "category": "GPU", "condition": "new", "seller_id": admin.id, "location": "Chicago, IL"},
            {"title": "Custom Watercooled Gaming Rig", "price": 3499.99, "category": "PC", "condition": "used", "seller_id": seller.id, "location": "San Francisco, CA"},
            {"title": "Samsung 990 Pro 2TB NVMe", "price": 169.99, "category": "Storage", "condition": "new", "seller_id": admin.id, "location": "Denver, CO"},
            {"title": "Xbox Series X", "price": 449.99, "category": "Console", "condition": "new", "seller_id": seller.id, "location": "Portland, OR"},
            {"title": "NZXT H7 Flow White Case", "price": 99.99, "category": "Accessory", "condition": "new", "seller_id": admin.id, "location": "Dallas, TX"},
        ]
        count = 0
        for p in products:
            if self._exists_marketplace_product(p["title"]):
                continue
            product = Product(
                id=str(uuid.uuid4()),
                title=p["title"],
                price=p["price"],
                category=p["category"],
                condition=p["condition"],
                seller_id=p["seller_id"],
                location=p.get("location", ""),
                description=p.get("description", fake_description(p["title"], "", p["category"])),
                images=p.get("images", []),
                specs=p.get("specs", {}),
                is_available=True,
            )
            self.db.add(product)
            count += 1
        self.db.flush()
        self.stats["marketplace_products"] += count
        return count

    # ---------- Bulk Run ----------

    def run_all(self, include_users: bool = True, include_communities: bool = True, include_catalog: bool = True, include_marketplace: bool = True, include_generated_catalog: bool = True):
        if include_catalog:
            self.seed_categories()
            self.seed_subcategories()
            self.seed_products()

        if include_generated_catalog:
            count = self.seed_catalog()
            print(f"  Catalog generator: {count} parts added")

        if include_users:
            self.seed_users()

        if include_communities:
            self.seed_communities()

        if include_marketplace:
            self.seed_marketplace_products()

        self.db.commit()
        return self.stats


def run_seed(db: Session | None = None, **kwargs) -> dict:
    """Standalone entry point: seeds the database with all data."""
    if db is None:
        init_db()
        db = SessionLocal()
        close = True
    else:
        close = False

    try:
        engine = SeedEngine(db)
        stats = engine.run_all(**kwargs)
        return stats
    finally:
        if close:
            db.close()


def clear_all(db: Session | None = None):
    """Clear all seedable data (for re-seeding)."""
    if db is None:
        init_db()
        db = SessionLocal()
        close = True
    else:
        close = False

    try:
        for table in [Product, PCPart, Subcategory, Category, Community, User]:
            db.query(table).delete()
        db.commit()
    finally:
        if close:
            db.close()


if __name__ == "__main__":
    stats = run_seed()
    print(f"Seed complete: {stats}")
