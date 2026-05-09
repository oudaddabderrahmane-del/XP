from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, EmailStr

from config.database import get_db
from models.models import User, Product, Review, Community, Post, Comment, Message, PCPart, Build, Favorite, Notification, Order, APIKey, community_members, Category, Subcategory
import secrets
from utils.auth import hash_password, verify_password, create_access_token, decode_token
from utils.helpers import generate_id, calculate_level
from seeds.seeder import SeedEngine

router = APIRouter()

# ========== Schemas ==========

class RegisterReq(BaseModel):
    username: str
    email: str
    password: str

class LoginReq(BaseModel):
    email: str
    password: str

class ProductReq(BaseModel):
    title: str
    description: str = ""
    price: float
    category: str = "Other"
    condition: str = "new"
    images: list = []
    location: str = ""
    specs: dict = {}

class ReviewReq(BaseModel):
    rating: int
    comment: str = ""

class CommunityReq(BaseModel):
    name: str
    description: str = ""
    icon: str = ""
    is_private: bool = False

class PostReq(BaseModel):
    title: str
    content: str = ""
    community_id: str = ""
    images: list = []

class CommentReq(BaseModel):
    content: str

class MessageReq(BaseModel):
    receiver_id: str
    content: str

class BuildReq(BaseModel):
    name: str
    description: str = ""
    parts: list = []
    total_price: float = 0
    is_public: bool = False

class PCPartReq(BaseModel):
    name: str
    category: str
    manufacturer: str = ""
    model: str = ""
    specs: dict = {}
    price: float = 0
    power_consumption: int = 0

# ========== Helpers ==========

def get_current_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        return None
    try:
        payload = decode_token(authorization.split(" ")[1])
        user = db.query(User).filter(User.id == payload.get("sub")).first()
        return user
    except Exception:
        return None

def user_to_dict(u):
    return {
        "id": u.id, "username": u.username, "email": u.email,
        "avatar": u.avatar, "bio": u.bio, "location": u.location,
        "xp": u.xp, "level": u.level, "badges": u.badges or [],
        "followers": len(u.followers_rel) if hasattr(u, 'followers_rel') else 0,
        "following": len(u.following_rel) if hasattr(u, 'following_rel') else 0,
        "role": u.role, "is_verified": u.is_verified, "is_seller": u.is_seller,
        "created_at": u.created_at.isoformat() if u.created_at else "",
    }

def product_to_dict(p):
    return {
        "id": p.id, "title": p.title, "description": p.description,
        "price": p.price, "condition": p.condition, "category": p.category,
        "images": p.images or [], "seller_id": p.seller_id,
        "location": p.location, "specs": p.specs or {},
        "is_available": p.is_available, "views": p.views, "favorites": p.favorites,
        "rating": p.rating, "reviews_count": p.reviews_count,
        "created_at": p.created_at.isoformat() if p.created_at else "",
    }

def community_to_dict(c):
    return {
        "id": c.id, "name": c.name, "description": c.description,
        "icon": c.icon, "owner_id": c.owner_id,
        "member_count": c.member_count, "is_private": c.is_private,
        "created_at": c.created_at.isoformat() if c.created_at else "",
    }

def post_to_dict(p):
    return {
        "id": p.id, "title": p.title, "content": p.content,
        "author_id": p.author_id, "community_id": p.community_id,
        "images": p.images or [], "upvotes": p.upvotes, "downvotes": p.downvotes,
        "comments_count": p.comments_count,
        "created_at": p.created_at.isoformat() if p.created_at else "",
    }

def build_to_dict(b):
    return {
        "id": b.id, "user_id": b.user_id, "name": b.name,
        "description": b.description, "parts": b.parts or [],
        "total_price": b.total_price, "is_public": b.is_public,
        "likes": b.likes,
        "created_at": b.created_at.isoformat() if b.created_at else "",
    }

def pcpart_to_dict(p):
    return {
        "id": p.id, "name": p.name, "brand": p.brand,
        "category": p.category, "category_id": p.category_id,
        "subcategory_id": p.subcategory_id,
        "manufacturer": p.manufacturer, "model": p.model,
        "specs": p.specs or {}, "price": p.price,
        "power_consumption": p.power_consumption,
        "compatibility": p.compatibility or {},
        "image_url": p.image_url,
        "stock_status": p.stock_status,
        "is_active": p.is_active,
        "created_at": p.created_at.isoformat() if p.created_at else "",
    }

# ========== Auth Routes ==========

@router.post("/api/auth/register")
def register(data: RegisterReq, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.email == data.email) | (User.username == data.username)
    ).first()
    if existing:
        raise HTTPException(400, "User already exists")
    user = User(
        id=generate_id(), username=data.username, email=data.email,
        hashed_password=hash_password(data.password), xp=0, level=1,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "user": user_to_dict(user)}

@router.post("/api/auth/login")
def login(data: LoginReq, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "user": user_to_dict(user)}

@router.get("/api/auth/me")
def get_me(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    return user_to_dict(user)

# ========== User Routes ==========

class UpdateProfileReq(BaseModel):
    bio: str = ""
    location: str = ""
    avatar: str = ""

@router.patch("/api/users/me")
def update_profile(data: UpdateProfileReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    if data.bio:
        user.bio = data.bio
    if data.location:
        user.location = data.location
    if data.avatar:
        user.avatar = data.avatar
    db.commit()
    db.refresh(user)
    return user_to_dict(user)

@router.get("/api/users")
def list_users(search: str = "", db: Session = Depends(get_db)):
    query = db.query(User).order_by(User.xp.desc())
    if search:
        query = query.filter(User.username.ilike(f"%{search}%"))
    users = query.limit(50).all()
    return {"users": [user_to_dict(u) for u in users]}

@router.get("/api/users/{user_id}/stats")
def get_user_stats(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    products_count = db.query(Product).filter(Product.seller_id == user_id).count()
    builds_count = db.query(Build).filter(Build.user_id == user_id).count()
    return {
        "products": products_count,
        "builds": builds_count,
        "followers": len(user.followers_rel) if hasattr(user, 'followers_rel') else 0,
        "following": len(user.following_rel) if hasattr(user, 'following_rel') else 0,
    }

@router.get("/api/users/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user_to_dict(user)

# ========== Product Routes ==========

@router.post("/api/products")
def create_product(data: ProductReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    product = Product(
        id=generate_id(), title=data.title, description=data.description,
        price=data.price, category=data.category, condition=data.condition,
        images=data.images, location=data.location, specs=data.specs,
        seller_id=user.id if user else None,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"product": product_to_dict(product)}

@router.get("/api/products")
def list_products(category: str = "", search: str = "", sort: str = "newest", skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    query = db.query(Product).filter(Product.is_available == True)
    if category:
        query = query.filter(Product.category == category)
    if search:
        query = query.filter(
            Product.title.ilike(f"%{search}%") | Product.description.ilike(f"%{search}%")
        )
    if sort == "price_asc":
        query = query.order_by(Product.price.asc())
    elif sort == "price_desc":
        query = query.order_by(Product.price.desc())
    else:
        query = query.order_by(desc(Product.created_at))
    total = query.count()
    products = query.offset(skip).limit(limit).all()
    return {"products": [product_to_dict(p) for p in products], "total": total}

@router.get("/api/products/{product_id}")
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    product.views = (product.views or 0) + 1
    db.commit()
    return product_to_dict(product)

@router.delete("/api/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    db.delete(product)
    db.commit()
    return {"status": "deleted"}

# ========== Review Routes ==========

@router.post("/api/products/{product_id}/reviews")
def create_review(product_id: str, data: ReviewReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    review = Review(id=generate_id(), product_id=product_id, user_id=user.id if user else "anon",
                    rating=data.rating, comment=data.comment)
    db.add(review)
    product.reviews_count = (product.reviews_count or 0) + 1
    product.rating = (product.rating or 0) * (product.reviews_count - 1) + data.rating / product.reviews_count
    db.commit()
    return {"status": "ok", "review": {"id": review.id, "rating": review.rating, "comment": review.comment}}

# ========== Favorite Routes ==========

@router.post("/api/favorites/{product_id}")
def toggle_favorite(product_id: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    existing = db.query(Favorite).filter(Favorite.user_id == user.id, Favorite.product_id == product_id).first()
    if existing:
        db.delete(existing)
        product.favorites = max(0, (product.favorites or 0) - 1)
        db.commit()
        return {"favorited": False}
    else:
        fav = Favorite(id=generate_id(), user_id=user.id, product_id=product_id)
        db.add(fav)
        product.favorites = (product.favorites or 0) + 1
        db.commit()
        return {"favorited": True}

@router.get("/api/favorites")
def list_favorites(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    favs = db.query(Favorite).filter(Favorite.user_id == user.id).all()
    product_ids = [f.product_id for f in favs]
    products = db.query(Product).filter(Product.id.in_(product_ids)).all() if product_ids else []
    return {"favorites": [product_to_dict(p) for p in products]}

# ========== Notification Routes ==========

@router.get("/api/notifications")
def list_notifications(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    notifs = db.query(Notification).filter(Notification.user_id == user.id).order_by(desc(Notification.created_at)).limit(50).all()
    return {"notifications": [{
        "id": n.id, "type": n.type, "title": n.title, "content": n.content,
        "reference_id": n.reference_id, "is_read": n.is_read,
        "created_at": n.created_at.isoformat() if n.created_at else ""
    } for n in notifs]}

@router.post("/api/notifications/{notif_id}/read")
def mark_notification_read(notif_id: str, db: Session = Depends(get_db)):
    notif = db.query(Notification).filter(Notification.id == notif_id).first()
    if notif:
        notif.is_read = True
        db.commit()
    return {"status": "ok"}

@router.post("/api/notifications/read-all")
def mark_all_read(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    db.query(Notification).filter(Notification.user_id == user.id, Notification.is_read == False).update({"is_read": True})
    db.commit()
    return {"status": "ok"}

# ========== Order Routes ==========

class OrderReq(BaseModel):
    product_id: str
    quantity: int = 1
    delivery_address: str = ""
    payment_method: str = "cash"

@router.post("/api/orders")
def create_order(data: OrderReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    product = db.query(Product).filter(Product.id == data.product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    order = Order(
        id=generate_id(), buyer_id=user.id, seller_id=product.seller_id or "",
        product_id=data.product_id, quantity=data.quantity,
        total_price=product.price * data.quantity, status="pending",
        delivery_address=data.delivery_address, payment_method=data.payment_method,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return {"order": {
        "id": order.id, "product_id": order.product_id, "total_price": order.total_price,
        "status": order.status, "created_at": order.created_at.isoformat() if order.created_at else ""
    }}

@router.get("/api/orders")
def list_orders(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    orders = db.query(Order).filter(
        (Order.buyer_id == user.id) | (Order.seller_id == user.id)
    ).order_by(desc(Order.created_at)).all()
    return {"orders": [{
        "id": o.id, "buyer_id": o.buyer_id, "seller_id": o.seller_id,
        "product_id": o.product_id, "quantity": o.quantity,
        "total_price": o.total_price, "status": o.status,
        "payment_method": o.payment_method, "is_paid": o.is_paid,
        "tracking_number": o.tracking_number,
        "created_at": o.created_at.isoformat() if o.created_at else ""
    } for o in orders]}

# ========== Community Routes ==========

@router.post("/api/communities")
def create_community(data: CommunityReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    existing = db.query(Community).filter(Community.name == data.name).first()
    if existing:
        raise HTTPException(400, "Community name taken")
    community = Community(
        id=generate_id(), name=data.name, description=data.description,
        icon=data.icon, owner_id=user.id if user else "anon", is_private=data.is_private,
    )
    db.add(community)
    db.commit()
    db.refresh(community)
    return {"community": community_to_dict(community)}

@router.get("/api/communities")
def list_communities(search: str = "", db: Session = Depends(get_db)):
    query = db.query(Community).order_by(desc(Community.member_count))
    if search:
        query = query.filter(Community.name.ilike(f"%{search}%"))
    return {"communities": [community_to_dict(c) for c in query.all()]}

@router.get("/api/communities/{community_id}")
def get_community(community_id: str, db: Session = Depends(get_db)):
    community = db.query(Community).filter(Community.id == community_id).first()
    if not community:
        raise HTTPException(404, "Community not found")
    return community_to_dict(community)

# ========== Community Membership Routes ==========

@router.post("/api/communities/{community_id}/join")
def join_community(community_id: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    community = db.query(Community).filter(Community.id == community_id).first()
    if not community:
        raise HTTPException(404, "Community not found")
    existing = db.query(community_members).filter(
        community_members.c.user_id == user.id,
        community_members.c.community_id == community_id
    ).first()
    if existing:
        return {"status": "already_member"}
    stmt = community_members.insert().values(user_id=user.id, community_id=community_id)
    db.execute(stmt)
    community.member_count = (community.member_count or 0) + 1
    db.commit()
    return {"status": "joined"}

@router.post("/api/communities/{community_id}/leave")
def leave_community(community_id: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    community = db.query(Community).filter(Community.id == community_id).first()
    if not community:
        raise HTTPException(404, "Community not found")
    stmt = community_members.delete().where(
        community_members.c.user_id == user.id,
        community_members.c.community_id == community_id
    )
    db.execute(stmt)
    community.member_count = max(0, (community.member_count or 1) - 1)
    db.commit()
    return {"status": "left"}

@router.get("/api/user/communities")
def user_communities(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    joined = db.query(community_members).filter(community_members.c.user_id == user.id).all()
    community_ids = [r.community_id for r in joined]
    comms = db.query(Community).filter(Community.id.in_(community_ids)).all() if community_ids else []
    return {"communities": [community_to_dict(c) for c in comms]}

# ========== Post Routes ==========

@router.post("/api/posts")
def create_post(data: PostReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    post = Post(
        id=generate_id(), title=data.title, content=data.content,
        community_id=data.community_id, author_id=user.id if user else "anon",
        images=data.images,
    )
    db.add(post)
    if data.community_id:
        community = db.query(Community).filter(Community.id == data.community_id).first()
        if community:
            community.member_count = (community.member_count or 0) + 1
    db.commit()
    db.refresh(post)
    return {"post": post_to_dict(post)}

@router.get("/api/posts")
def list_posts(community_id: str = "", sort: str = "newest", skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    query = db.query(Post)
    if community_id:
        query = query.filter(Post.community_id == community_id)
    if sort == "top":
        query = query.order_by(desc(Post.upvotes - Post.downvotes))
    else:
        query = query.order_by(desc(Post.created_at))
    total = query.count()
    posts = query.offset(skip).limit(limit).all()
    return {"posts": [post_to_dict(p) for p in posts], "total": total}

@router.get("/api/posts/{post_id}")
def get_post(post_id: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(404, "Post not found")
    return post_to_dict(post)

@router.post("/api/posts/{post_id}/vote")
def vote_post(post_id: str, vote_type: str = "up", db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(404)
    if vote_type == "up":
        post.upvotes = (post.upvotes or 0) + 1
    else:
        post.downvotes = (post.downvotes or 0) + 1
    db.commit()
    return {"upvotes": post.upvotes, "downvotes": post.downvotes}

# ========== Comment Routes ==========

@router.post("/api/posts/{post_id}/comments")
def create_comment(post_id: str, data: CommentReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(404, "Post not found")
    comment = Comment(
        id=generate_id(), post_id=post_id, content=data.content,
        author_id=user.id if user else "anon",
    )
    db.add(comment)
    post.comments_count = (post.comments_count or 0) + 1
    db.commit()
    return {"comment": {"id": comment.id, "content": comment.content, "author_id": comment.author_id,
                        "created_at": comment.created_at.isoformat() if comment.created_at else ""}}

@router.get("/api/posts/{post_id}/comments")
def list_comments(post_id: str, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.created_at).all()
    return {"comments": [{"id": c.id, "content": c.content, "author_id": c.author_id,
                          "upvotes": c.upvotes, "downvotes": c.downvotes,
                          "created_at": c.created_at.isoformat() if c.created_at else ""} for c in comments]}

# ========== Message Routes ==========

@router.post("/api/messages")
def send_message(data: MessageReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    msg = Message(
        id=generate_id(), sender_id=user.id if user else "anon",
        receiver_id=data.receiver_id, content=data.content,
    )
    db.add(msg)
    db.commit()
    return {"message": {"id": msg.id, "sender_id": msg.sender_id, "receiver_id": msg.receiver_id,
                        "content": msg.content, "is_read": msg.is_read,
                        "created_at": msg.created_at.isoformat() if msg.created_at else ""}}

@router.get("/api/messages")
def list_messages(user=Depends(get_current_user), limit: int = 50, db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    messages = db.query(Message).filter(
        (Message.sender_id == user.id) | (Message.receiver_id == user.id)
    ).order_by(desc(Message.created_at)).limit(limit).all()
    messages.reverse()
    return {"messages": [{"id": m.id, "sender_id": m.sender_id, "receiver_id": m.receiver_id,
                          "content": m.content, "is_read": m.is_read,
                          "created_at": m.created_at.isoformat() if m.created_at else ""} for m in messages]}

# ========== API Key Routes ==========

@router.post("/api/keys")
def create_api_key(name: str = "Default", user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    raw_key = f"xp_api_{secrets.token_hex(24)}"
    api_key = APIKey(id=generate_id(), user_id=user.id, key=raw_key, name=name)
    db.add(api_key)
    db.commit()
    return {"key": raw_key, "id": api_key.id, "name": name}

@router.get("/api/keys")
def list_api_keys(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    keys = db.query(APIKey).filter(APIKey.user_id == user.id).order_by(desc(APIKey.created_at)).all()
    return {"keys": [{"id": k.id, "name": k.name, "prefix": k.key[:20] + "...", "is_active": k.is_active, "last_used": k.last_used.isoformat() if k.last_used else None, "created_at": k.created_at.isoformat() if k.created_at else ""} for k in keys]}

@router.delete("/api/keys/{key_id}")
def delete_api_key(key_id: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401, "Not authenticated")
    key = db.query(APIKey).filter(APIKey.id == key_id, APIKey.user_id == user.id).first()
    if not key:
        raise HTTPException(404)
    db.delete(key)
    db.commit()
    return {"status": "deleted"}

# ========== PC Part Routes ==========

@router.post("/api/parts")
def create_pcpart(data: PCPartReq, db: Session = Depends(get_db)):
    part = PCPart(id=generate_id(), name=data.name, category=data.category,
                  manufacturer=data.manufacturer, model=data.model,
                  specs=data.specs, price=data.price, power_consumption=data.power_consumption)
    db.add(part)
    db.commit()
    db.refresh(part)
    return {"part": pcpart_to_dict(part)}

@router.get("/api/parts")
def list_pcparts(category: str = "", search: str = "", db: Session = Depends(get_db)):
    query = db.query(PCPart)
    if category:
        query = query.filter(PCPart.category == category)
    if search:
        query = query.filter(PCPart.name.ilike(f"%{search}%"))
    return {"parts": [pcpart_to_dict(p) for p in query.all()]}

@router.get("/api/parts/{part_id}")
def get_pcpart(part_id: str, db: Session = Depends(get_db)):
    part = db.query(PCPart).filter(PCPart.id == part_id).first()
    if not part:
        raise HTTPException(404)
    return pcpart_to_dict(part)

# ========== Build Routes ==========

@router.post("/api/builds")
def create_build(data: BuildReq, user=Depends(get_current_user), db: Session = Depends(get_db)):
    build = Build(id=generate_id(), name=data.name, description=data.description,
                  parts=data.parts, total_price=data.total_price,
                  is_public=data.is_public, user_id=user.id if user else "anon")
    db.add(build)
    db.commit()
    db.refresh(build)
    return {"build": build_to_dict(build)}

@router.get("/api/builds")
def list_builds(public: bool = True, db: Session = Depends(get_db)):
    query = db.query(Build)
    if public:
        query = query.filter(Build.is_public == True)
    query = query.order_by(desc(Build.created_at))
    return {"builds": [build_to_dict(b) for b in query.all()]}

@router.get("/api/builds/{build_id}")
def get_build(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(404)
    return build_to_dict(build)

@router.delete("/api/builds/{build_id}")
def delete_build(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(404)
    db.delete(build)
    db.commit()
    return {"status": "deleted"}

# ========== AI Routes ==========

@router.post("/api/ai/compatibility")
def ai_compatibility(data: dict):
    parts = data.get("parts", data.get("data", data))
    if isinstance(parts, dict):
        parts = [parts]
    if not isinstance(parts, list):
        parts = []
    issues = []
    warnings = []
    categories = {p.get("category", ""): p for p in parts}
    if "CPU" in categories and "Motherboard" in categories:
        cpu = categories["CPU"]
        mb = categories["Motherboard"]
        cpu_name = cpu.get("name", "").lower()
        mb_name = mb.get("name", "").lower()
        if "intel" in cpu_name and "intel" not in mb_name and "amd" not in cpu_name:
            warnings.append("Intel CPU with non-Intel chipset motherboard — verify socket compatibility")
        if "amd" in cpu_name and "amd" not in mb_name and "intel" not in cpu_name:
            warnings.append("AMD CPU with non-AMD chipset motherboard — verify socket compatibility")
    gpus = [p for p in parts if p.get("category") == "GPU"]
    psus = [p for p in parts if p.get("category") == "PSU"]
    if gpus and psus:
        gpu_power = gpus[0].get("power_consumption", 200)
        psu_wattage = psus[0].get("power_consumption", 500)
        if gpu_power > psu_wattage * 0.8:
            issues.append(f"GPU power draw ({gpu_power}W) may exceed PSU capacity ({psu_wattage}W)")
    return {"compatible": len(issues) == 0, "issues": issues, "warnings": warnings}

@router.post("/api/ai/recommend")
def ai_recommend(budget: float = 1000, use_case: str = "gaming"):
    tiers = {
        "gaming": {
            "budget": [
                {"category": "CPU", "name": "Ryzen 5 5600", "price": 120},
                {"category": "GPU", "name": "RTX 3060", "price": 250},
                {"category": "RAM", "name": "16GB DDR4", "price": 50},
                {"category": "Motherboard", "name": "B550", "price": 100},
                {"category": "PSU", "name": "550W 80+", "price": 60},
                {"category": "Storage", "name": "500GB SSD", "price": 40},
            ],
            "mid": [
                {"category": "CPU", "name": "Ryzen 5 7600X", "price": 220},
                {"category": "GPU", "name": "RTX 4070", "price": 550},
                {"category": "RAM", "name": "32GB DDR5", "price": 100},
                {"category": "Motherboard", "name": "B650", "price": 150},
                {"category": "PSU", "name": "750W 80+ Gold", "price": 100},
                {"category": "Storage", "name": "1TB NVMe", "price": 80},
            ],
            "high": [
                {"category": "CPU", "name": "Ryzen 7 7800X3D", "price": 400},
                {"category": "GPU", "name": "RTX 4090", "price": 1600},
                {"category": "RAM", "name": "64GB DDR5", "price": 200},
                {"category": "Motherboard", "name": "X670E", "price": 300},
                {"category": "PSU", "name": "1000W 80+ Platinum", "price": 200},
                {"category": "Storage", "name": "2TB NVMe", "price": 150},
            ],
        },
        "office": {
            "budget": [
                {"category": "CPU", "name": "Intel i3-14100", "price": 100},
                {"category": "RAM", "name": "8GB DDR4", "price": 30},
                {"category": "Motherboard", "name": "H610", "price": 80},
                {"category": "PSU", "name": "400W", "price": 40},
                {"category": "Storage", "name": "256GB SSD", "price": 25},
            ],
            "mid": [
                {"category": "CPU", "name": "Intel i5-14400", "price": 200},
                {"category": "RAM", "name": "16GB DDR4", "price": 50},
                {"category": "Motherboard", "name": "B760", "price": 120},
                {"category": "PSU", "name": "500W", "price": 50},
                {"category": "Storage", "name": "512GB SSD", "price": 40},
            ],
        },
        "streaming": {
            "mid": [
                {"category": "CPU", "name": "Ryzen 7 7700X", "price": 300},
                {"category": "GPU", "name": "RTX 4070", "price": 550},
                {"category": "RAM", "name": "32GB DDR5", "price": 100},
                {"category": "Motherboard", "name": "B650", "price": 150},
                {"category": "PSU", "name": "750W 80+ Gold", "price": 100},
                {"category": "Storage", "name": "1TB NVMe", "price": 80},
            ],
        },
    }
    use_case = use_case.lower()
    if use_case not in tiers:
        use_case = "gaming"
    if budget >= 2000:
        tier = "high"
    elif budget >= 1000:
        tier = "mid"
    else:
        tier = "budget"
    parts = tiers.get(use_case, {}).get(tier, [])
    total = sum(p["price"] for p in parts)
    return {"parts": parts, "total_price": total, "remaining": budget - total, "tier": tier}

@router.get("/api/ai/price-analysis/{product_id}")
def ai_price_analysis(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404)
    benchmarks = {
        "GPU": {"low": 150, "mid": 400, "high": 800},
        "CPU": {"low": 100, "mid": 300, "high": 600},
        "RAM": {"low": 30, "mid": 80, "high": 200},
        "Motherboard": {"low": 80, "mid": 200, "high": 400},
        "Storage": {"low": 30, "mid": 80, "high": 200},
        "PSU": {"low": 40, "mid": 100, "high": 200},
    }
    bench = benchmarks.get(product.category, {"low": 50, "mid": 200, "high": 500})
    price = product.price
    if price <= bench["low"]:
        status, analysis = "great_deal", f"Excellent price! Well below market average."
    elif price <= bench["mid"]:
        status, analysis = "fair_price", f"Fair market price within typical range."
    elif price <= bench["high"]:
        status, analysis = "slightly_high", f"Price is above average. Compare with other listings."
    else:
        status, analysis = "overpriced", f"Significantly above market price."
    return {"status": status, "analysis": analysis, "benchmark": bench}

# ========== Image Upload ==========
@router.post("/api/products/upload-image")
async def upload_image(file: bytes = None):
    import uuid, shutil, os
    from fastapi import UploadFile, File
    # Keep compatibility with existing frontend
    return {"url": ""}

# ========== Forum Routes (gg-platform compatibility) ==========
class ForumThreadCreate(BaseModel):
    title: str
    username: str
    content: str = ""
    category: str = "General"

class ForumPostCreate(BaseModel):
    username: str
    content: str

@router.post("/api/forums/threads")
def create_forum_thread(data: ForumThreadCreate, db: Session = Depends(get_db)):
    post = Post(id=generate_id(), title=data.title, content=data.content, community_id="")
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"status": "ok", "thread": {
        "id": post.id, "title": post.title, "username": data.username,
        "content": post.content, "category": data.category, "post_count": 0,
        "created_at": post.created_at.isoformat() if post.created_at else ""
    }}

@router.get("/api/forums/threads")
def list_forum_threads(category: str = "", db: Session = Depends(get_db)):
    query = db.query(Post).order_by(desc(Post.created_at))
    if category:
        query = query.filter(Post.title.ilike(f"%{category}%"))
    posts = query.all()
    return {"threads": [{"id": p.id, "title": p.title, "username": "Anonymous",
                         "content": p.content, "category": "General", "post_count": 0,
                         "created_at": p.created_at.isoformat() if p.created_at else ""} for p in posts]}

@router.get("/api/forums/threads/{thread_id}")
def get_forum_thread(thread_id: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == thread_id).first()
    if not post:
        raise HTTPException(404)
    return {"id": post.id, "title": post.title, "username": "Anonymous",
            "content": post.content, "category": "General", "post_count": 0,
            "created_at": post.created_at.isoformat() if post.created_at else ""}

@router.post("/api/forums/threads/{thread_id}/posts")
def create_forum_post(thread_id: str, data: ForumPostCreate, db: Session = Depends(get_db)):
    comment = Comment(id=generate_id(), post_id=thread_id, content=data.content, author_id="")
    db.add(comment)
    db.commit()
    return {"status": "ok", "post": {"id": comment.id, "thread_id": thread_id, 
             "username": data.username, "content": comment.content,
             "created_at": comment.created_at.isoformat() if comment.created_at else ""}}

@router.get("/api/forums/threads/{thread_id}/posts")
def list_forum_posts(thread_id: str, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.post_id == thread_id).order_by(Comment.created_at).all()
    return {"posts": [{"id": c.id, "thread_id": thread_id, "username": "Anonymous",
                       "content": c.content, "created_at": c.created_at.isoformat() if c.created_at else ""} for c in comments]}

# ========== Guide Routes (gg-platform compatibility) ==========
seed_guides = [
    {"title": "First PC Build: A Complete Beginner Guide", "category": "Beginner", "difficulty": "Beginner",
     "content": "Step-by-step walkthrough for assembling your first desktop PC.", "username": "gg"},
    {"title": "PC Building Tips & Tricks", "category": "General", "difficulty": "Intermediate",
     "content": "Professional tips for cable management and airflow optimization.", "username": "gg"},
    {"title": "How to Choose the Right GPU", "category": "PC Building", "difficulty": "Advanced",
     "content": "Deep dive into GPU architecture and performance benchmarks.", "username": "gg"},
]

@router.post("/api/guides")
def create_guide(data: dict, db: Session = Depends(get_db)):
    return {"status": "ok", "guide": {"id": generate_id(), "title": data.get("title", ""),
            "content": data.get("content", ""), "category": data.get("category", "General"),
            "difficulty": data.get("difficulty", "Beginner"), "username": data.get("username", "gg"),
            "created_at": datetime.now(timezone.utc).isoformat()}}

@router.get("/api/guides")
def list_guides(category: str = ""):
    guides = seed_guides
    if category and category != "All":
        guides = [g for g in guides if g["category"] == category]
    return {"guides": guides}

# ========== Build Estimation ==========

@router.post("/api/ai/build-estimate")
def ai_build_estimate(data: dict):
    parts = {p.get("category", ""): p for p in data.get("parts", []) if isinstance(p, dict)}
    cpu = parts.get("CPU", {})
    gpu = parts.get("GPU", {})
    ram = parts.get("RAM", {})
    
    # FPS Estimation
    gpu_name = gpu.get("name", "").lower()
    if "4090" in gpu_name:
        fps_1080p, fps_1440p, fps_4k = 240, 180, 120
    elif "4070" in gpu_name:
        fps_1080p, fps_1440p, fps_4k = 180, 130, 80
    elif "4060" in gpu_name or "3060" in gpu_name:
        fps_1080p, fps_1440p, fps_4k = 140, 95, 55
    elif "3080" in gpu_name or "7800" in gpu_name:
        fps_1080p, fps_1440p, fps_4k = 200, 150, 95
    elif "7900" in gpu_name:
        fps_1080p, fps_1440p, fps_4k = 220, 160, 105
    else:
        gpu_price = gpu.get("price", 0)
        if gpu_price > 800:
            fps_1080p, fps_1440p, fps_4k = 200, 140, 90
        elif gpu_price > 400:
            fps_1080p, fps_1440p, fps_4k = 140, 95, 55
        else:
            fps_1080p, fps_1440p, fps_4k = 90, 60, 35
    
    # Bottleneck estimation
    cpu_name = cpu.get("name", "").lower()
    bottleneck_pct = 0
    bottleneck_note = "Balanced build"
    
    if gpu_name and cpu_name:
        gpu_tier = 5 if "4090" in gpu_name else (4 if "4080" in gpu_name or "7900" in gpu_name else (3 if "4070" in gpu_name or "7800" in gpu_name else 2))
        cpu_tier = 5 if "7800x3d" in cpu_name or "14900k" in cpu_name or "13900k" in cpu_name else (4 if "13700k" in cpu_name or "7700x" in cpu_name or "7600x" in cpu_name else (3 if "13600k" in cpu_name or "5600x" in cpu_name else 2))
        
        if gpu_tier > cpu_tier + 1:
            bottleneck_pct = (gpu_tier - cpu_tier) * 8
            bottleneck_note = f"GPU may be bottlenecked by CPU (~{bottleneck_pct}% loss)"
        elif cpu_tier > gpu_tier + 1:
            bottleneck_pct = (cpu_tier - gpu_tier) * 5
            bottleneck_note = f"CPU may bottleneck GPU (~{bottleneck_pct}% loss)"
        elif gpu_tier >= 4 and cpu_tier >= 4:
            bottleneck_note = "Great balance for high-end gaming"
        else:
            bottleneck_note = "Well-balanced mid-range build"
    
    # Temperature estimation
    gpu_power = gpu.get("power_consumption", 200)
    cpu_power = cpu.get("power_consumption", 100)
    total_power = gpu_power + cpu_power + (ram.get("power_consumption", 10) * 2)
    
    if total_power > 600:
        temp_estimate = "High (70-85°C) — Consider liquid cooling"
    elif total_power > 400:
        temp_estimate = "Moderate (60-75°C) — Air cooling sufficient"
    elif total_power > 250:
        temp_estimate = "Low (50-65°C) — Stock cooling OK"
    else:
        temp_estimate = "Very Low (40-55°C) — Efficient build"
    
    return {
        "fps": {"1080p": fps_1080p, "1440p": fps_1440p, "4k": fps_4k},
        "bottleneck": {"percentage": bottleneck_pct, "note": bottleneck_note},
        "temperature": temp_estimate,
        "total_power_draw": total_power,
    }

# ========== AI endpoints (gg-platform compatibility) ==========
@router.post("/api/ai/check-compatibility")
def ai_check_compat(data: dict, db: Session = Depends(get_db)):
    parts_list = data.get("parts", [])
    issues = []
    warnings = []
    for p in parts_list:
        title = p.get("title", "").lower()
        if "13700k" in title and "z790" not in str(p.get("subcategory", "")).lower():
            warnings.append("CPU socket LGA1700 may not match motherboard")
    return {"compatible": len(issues) == 0, "issues": issues, "warnings": warnings,
            "estimated_power": 450}

@router.post("/api/ai/smart-search")
def ai_smart_search(data: dict, db: Session = Depends(get_db)):
    query = data.get("query", "").lower()
    products = db.query(Product).filter(Product.is_available == True).all()
    results = []
    for p in products:
        if query in p.title.lower() or query in (p.description or "").lower():
            results.append(product_to_dict(p))
    return {"results": results[:20], "query": query, "count": len(results[:20])}

@router.post("/api/ai/recommend-build")
def ai_recommend_build(data: dict):
    budget = data.get("budget", 1000)
    use_case = data.get("use_case", "Gaming")
    gaming_parts = {
        "500": [
            {"subcategory": "CPUs", "hint": "Ryzen 5 5600X", "title": "Ryzen 5 5600X", "price": 130, "max_price": 130},
            {"subcategory": "Motherboards", "hint": "B550", "title": "B550 Motherboard", "price": 100, "max_price": 100},
            {"subcategory": "RAM", "hint": "16GB DDR4", "title": "16GB DDR4", "price": 50, "max_price": 50},
            {"subcategory": "GPUs (Graphics Cards)", "hint": "RTX 3060", "title": "RTX 3060", "price": 200, "max_price": 200},
            {"subcategory": "SSD / HDD", "hint": "500GB SSD", "title": "500GB SSD", "price": 40, "max_price": 40},
            {"subcategory": "Power Supplies", "hint": "500W 80+", "title": "500W PSU", "price": 50, "max_price": 50},
        ],
        "1000": [
            {"subcategory": "CPUs", "hint": "Ryzen 5 7600X", "title": "Ryzen 5 7600X", "price": 220, "max_price": 220},
            {"subcategory": "Motherboards", "hint": "B650", "title": "B650 Motherboard", "price": 150, "max_price": 150},
            {"subcategory": "RAM", "hint": "16GB DDR5", "title": "16GB DDR5", "price": 80, "max_price": 80},
            {"subcategory": "GPUs (Graphics Cards)", "hint": "RTX 4070", "title": "RTX 4070", "price": 550, "max_price": 550},
            {"subcategory": "SSD / HDD", "hint": "1TB NVMe", "title": "1TB NVMe", "price": 70, "max_price": 70},
            {"subcategory": "Power Supplies", "hint": "750W 80+ Gold", "title": "750W PSU", "price": 100, "max_price": 100},
        ],
        "2000": [
            {"subcategory": "CPUs", "hint": "Ryzen 7 7800X3D", "title": "Ryzen 7 7800X3D", "price": 400, "max_price": 400},
            {"subcategory": "Motherboards", "hint": "X670E", "title": "X670E Motherboard", "price": 300, "max_price": 300},
            {"subcategory": "RAM", "hint": "32GB DDR5", "title": "32GB DDR5", "price": 150, "max_price": 150},
            {"subcategory": "GPUs (Graphics Cards)", "hint": "RTX 4090", "title": "RTX 4090", "price": 1600, "max_price": 1600},
            {"subcategory": "SSD / HDD", "hint": "2TB NVMe", "title": "2TB NVMe", "price": 120, "max_price": 120},
            {"subcategory": "Power Supplies", "hint": "1000W 80+ Platinum", "title": "1000W PSU", "price": 200, "max_price": 200},
        ],
    }
    if budget >= 1500:
        tier = "2000"
    elif budget >= 800:
        tier = "1000"
    else:
        tier = "500"
    parts = gaming_parts.get(tier, [])
    total = sum(p["price"] for p in parts)
    return {"recommended_parts": parts, "total_price": total, "budget": budget, "use_case": use_case}

# ========== Seed Data ==========

@router.post("/api/seed")
def seed_data(db: Session = Depends(get_db)):
    engine = SeedEngine(db)
    stats = engine.run_all()
    return {"message": "Database seeded successfully!", "stats": stats}

@router.post("/seed-db")
def seed_db(db: Session = Depends(get_db)):
    engine = SeedEngine(db)
    stats = engine.run_all()
    return {"message": "Database seeded successfully!", "stats": stats}

@router.post("/seed-db/clear")
def clear_seed_data(db: Session = Depends(get_db)):
    for table in [Product, PCPart, Subcategory, Category, Community, User]:
        db.query(table).delete()
    db.commit()
    return {"message": "All seed data cleared"}

@router.get("/api/categories")
def list_categories(db: Session = Depends(get_db)):
    cats = db.query(Category).order_by(Category.sort_order).all()
    return {"categories": [{
        "id": c.id, "name": c.name, "slug": c.slug, "icon": c.icon,
        "description": c.description, "sort_order": c.sort_order,
    } for c in cats]}

@router.get("/api/categories/{category_id}/subcategories")
def list_subcategories(category_id: str, db: Session = Depends(get_db)):
    subs = db.query(Subcategory).filter(Subcategory.category_id == category_id).order_by(Subcategory.sort_order).all()
    return {"subcategories": [{
        "id": s.id, "name": s.name, "slug": s.slug, "category_id": s.category_id,
        "description": s.description, "sort_order": s.sort_order,
    } for s in subs]}
