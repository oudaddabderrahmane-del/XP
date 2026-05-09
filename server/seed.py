"""Seed the database with initial data"""
import uuid
from config.database import init_db, SessionLocal
from models.models import User, PCPart, Product, Community
from utils.auth import hash_password

init_db()
db = SessionLocal()

try:
    if db.query(User).count() > 0:
        print(f"Database already has {db.query(User).count()} users, skipping seed")
        exit(0)

    admin = User(id=str(uuid.uuid4()), username="admin", email="admin@xp.game",
                 hashed_password=hash_password("admin123"), role="admin", xp=9999, level=50)
    user1 = User(id=str(uuid.uuid4()), username="gamer1", email="gamer@xp.game",
                 hashed_password=hash_password("password123"), xp=500, level=10)
    user2 = User(id=str(uuid.uuid4()), username="techdev", email="dev@xp.game",
                 hashed_password=hash_password("dev123"), xp=1200, level=20)
    extra_users = [
        {"username": "PixelMaster", "email": "pixel@xp.game", "xp": 7500, "level": 35, "role": "moderator", "bio": "PC building enthusiast & photographer"},
        {"username": "CodeWizard", "email": "wizard@xp.game", "xp": 6200, "level": 30, "role": "user", "bio": "Full-stack dev & gaming hardware collector"},
        {"username": "NeonRider", "email": "neon@xp.game", "xp": 4800, "level": 25, "role": "user", "bio": "RGB everything | Cyberpunk lover"},
        {"username": "BuildMaster", "email": "build@xp.game", "xp": 3500, "level": 22, "role": "verified_seller", "bio": "Custom PC builder since 2018"},
        {"username": "EliteGamer", "email": "elite@xp.game", "xp": 2800, "level": 18, "role": "user", "bio": "Competitive FPS gamer & streamer"},
        {"username": "DataStream", "email": "data@xp.game", "xp": 1900, "level": 15, "role": "user", "bio": "AI/ML engineer exploring hardware"},
        {"username": "CryptoVault", "email": "crypto@xp.game", "xp": 1500, "level": 13, "role": "verified_seller", "bio": "Hardware trader & crypto enthusiast"},
    ]
    all_users = [admin, user1, user2]
    for u_data in extra_users:
        u = User(id=str(uuid.uuid4()), username=u_data["username"], email=u_data["email"],
                 hashed_password=hash_password("password123"), xp=u_data["xp"], level=u_data["level"],
                 role=u_data.get("role", "user"), bio=u_data.get("bio", ""))
        all_users.append(u)
    db.add_all(all_users)
    db.commit()

    communities = [
        {"name": "PC Builders", "description": "Share and discuss PC builds", "owner_id": admin.id},
        {"name": "Gaming", "description": "Everything gaming", "owner_id": admin.id},
        {"name": "Developers", "description": "For devs and programmers", "owner_id": admin.id},
        {"name": "AI & Tech", "description": "AI discussions and tech news", "owner_id": user1.id},
    ]
    for c in communities:
        c["id"] = str(uuid.uuid4())
        db.add(Community(**c))
    db.commit()

    parts = [
        {"name": "Intel Core i7-13700K", "category": "CPU", "manufacturer": "Intel", "price": 449, "power_consumption": 253},
        {"name": "AMD Ryzen 7 7800X3D", "category": "CPU", "manufacturer": "AMD", "price": 389, "power_consumption": 120},
        {"name": "AMD Ryzen 5 7600X", "category": "CPU", "manufacturer": "AMD", "price": 219, "power_consumption": 105},
        {"name": "Intel Core i5-14600K", "category": "CPU", "manufacturer": "Intel", "price": 319, "power_consumption": 181},
        {"name": "NVIDIA RTX 4090", "category": "GPU", "manufacturer": "NVIDIA", "price": 1599, "power_consumption": 450},
        {"name": "NVIDIA RTX 4070 Ti Super", "category": "GPU", "manufacturer": "NVIDIA", "price": 799, "power_consumption": 285},
        {"name": "NVIDIA RTX 4070", "category": "GPU", "manufacturer": "NVIDIA", "price": 549, "power_consumption": 200},
        {"name": "AMD Radeon RX 7800 XT", "category": "GPU", "manufacturer": "AMD", "price": 499, "power_consumption": 263},
        {"name": "Corsair Vengeance 32GB DDR5", "category": "RAM", "manufacturer": "Corsair", "price": 109, "power_consumption": 10},
        {"name": "G.Skill Trident Z5 32GB DDR5", "category": "RAM", "manufacturer": "G.Skill", "price": 129, "power_consumption": 10},
        {"name": "Corsair Vengeance 16GB DDR4", "category": "RAM", "manufacturer": "Corsair", "price": 49, "power_consumption": 8},
        {"name": "ASUS ROG STRIX Z790-E", "category": "Motherboard", "manufacturer": "ASUS", "price": 399},
        {"name": "MSI MAG Z790 Tomahawk", "category": "Motherboard", "manufacturer": "MSI", "price": 259},
        {"name": "Gigabyte B650 AORUS Elite", "category": "Motherboard", "manufacturer": "Gigabyte", "price": 199},
        {"name": "Corsair RM850x 850W", "category": "PSU", "manufacturer": "Corsair", "price": 129, "power_consumption": 850},
        {"name": "EVGA SuperNOVA 1000 G7", "category": "PSU", "manufacturer": "EVGA", "price": 179, "power_consumption": 1000},
        {"name": "Seasonic Focus GX-750", "category": "PSU", "manufacturer": "Seasonic", "price": 99, "power_consumption": 750},
        {"name": "Samsung 990 Pro 2TB", "category": "Storage", "manufacturer": "Samsung", "price": 169, "power_consumption": 6},
        {"name": "WD Black SN850X 1TB", "category": "Storage", "manufacturer": "WD", "price": 109, "power_consumption": 5},
        {"name": "Samsung 870 EVO 1TB", "category": "Storage", "manufacturer": "Samsung", "price": 79, "power_consumption": 4},
        {"name": "NZXT H7 Flow", "category": "Case", "manufacturer": "NZXT", "price": 129},
        {"name": "Corsair 4000D Airflow", "category": "Case", "manufacturer": "Corsair", "price": 89},
        {"name": "Lian Li O11 Dynamic EVO", "category": "Case", "manufacturer": "Lian Li", "price": 149},
    ]
    for p in parts:
        p["id"] = str(uuid.uuid4())
        p["specs"] = {}
        p["model"] = p["name"]
        db.add(PCPart(**p))
    db.commit()

    products = [
        {"title": "RTX 4090 Gaming OC", "price": 1599, "category": "GPU", "condition": "new", "seller_id": user1.id, "location": "New York, NY"},
        {"title": "PlayStation 5 Digital", "price": 399, "category": "Console", "condition": "used", "seller_id": user1.id, "location": "Los Angeles, CA"},
        {"title": "Gaming PC RTX 4070 + i7", "price": 1299, "category": "PC", "condition": "new", "seller_id": user1.id, "location": "Austin, TX"},
        {"title": "Intel Core i7-13700K", "price": 449, "category": "CPU", "condition": "new", "seller_id": admin.id, "location": "Seattle, WA"},
        {"title": "Corsair 32GB DDR5 RAM", "price": 109, "category": "RAM", "condition": "new", "seller_id": admin.id, "location": "Miami, FL"},
        {"title": "ASUS ROG Strix RTX 4070 Ti", "price": 849, "category": "GPU", "condition": "new", "seller_id": admin.id, "location": "Chicago, IL"},
        {"title": "Custom Watercooled Gaming Rig", "price": 3499, "category": "PC", "condition": "used", "seller_id": user1.id, "location": "San Francisco, CA"},
        {"title": "Samsung 990 Pro 2TB NVMe", "price": 169, "category": "Storage", "condition": "new", "seller_id": admin.id, "location": "Denver, CO"},
        {"title": "Xbox Series X", "price": 449, "category": "Console", "condition": "new", "seller_id": user1.id, "location": "Portland, OR"},
        {"title": "NZXT H7 Flow White Case", "price": 99, "category": "Accessory", "condition": "new", "seller_id": admin.id, "location": "Dallas, TX"},
    ]
    for p in products:
        p["id"] = str(uuid.uuid4())
        p["images"] = []
        db.add(Product(**p))
    db.commit()
    print(f"Seeded: {db.query(User).count()} users, {db.query(PCPart).count()} parts, {db.query(Product).count()} products, {db.query(Community).count()} communities")
finally:
    db.close()
