from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Text, DateTime, Boolean, ForeignKey, Table, JSON
from sqlalchemy.orm import relationship
from config.database import Base
import uuid

def gen_id():
    return str(uuid.uuid4())

def utcnow():
    return datetime.now(timezone.utc)

followers = Table(
    'followers', Base.metadata,
    Column('follower_id', String, ForeignKey('users.id')),
    Column('following_id', String, ForeignKey('users.id')),
)

community_members = Table(
    'community_members', Base.metadata,
    Column('user_id', String, ForeignKey('users.id')),
    Column('community_id', String, ForeignKey('communities.id')),
)

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=gen_id)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    avatar = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    badges = Column(JSON, default=list)
    is_verified = Column(Boolean, default=False)
    is_seller = Column(Boolean, default=False)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=gen_id)
    title = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    condition = Column(String, default="new")
    category = Column(String, index=True)
    images = Column(JSON, default=list)
    seller_id = Column(String, ForeignKey('users.id'), nullable=True)
    location = Column(String, nullable=True)
    specs = Column(JSON, default=dict)
    is_available = Column(Boolean, default=True)
    views = Column(Integer, default=0)
    favorites = Column(Integer, default=0)
    rating = Column(Float, default=0)
    reviews_count = Column(Integer, default=0)
    seller = relationship("User", backref="products", foreign_keys=[seller_id])
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(String, primary_key=True, default=gen_id)
    product_id = Column(String, ForeignKey('products.id'))
    user_id = Column(String, ForeignKey('users.id'))
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(DateTime, default=utcnow)

class Community(Base):
    __tablename__ = "communities"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    icon = Column(String, nullable=True)
    owner_id = Column(String, ForeignKey('users.id'))
    member_count = Column(Integer, default=0)
    is_private = Column(Boolean, default=False)
    created_at = Column(DateTime, default=utcnow)

class Post(Base):
    __tablename__ = "posts"
    id = Column(String, primary_key=True, default=gen_id)
    title = Column(String, index=True)
    content = Column(Text)
    author_id = Column(String, ForeignKey('users.id'))
    community_id = Column(String, ForeignKey('communities.id'))
    images = Column(JSON, default=list)
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(String, primary_key=True, default=gen_id)
    post_id = Column(String, ForeignKey('posts.id'))
    author_id = Column(String, ForeignKey('users.id'))
    content = Column(Text)
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    created_at = Column(DateTime, default=utcnow)

class Message(Base):
    __tablename__ = "messages"
    id = Column(String, primary_key=True, default=gen_id)
    sender_id = Column(String, ForeignKey('users.id'))
    receiver_id = Column(String, ForeignKey('users.id'))
    content = Column(Text)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=utcnow)

class Category(Base):
    __tablename__ = "categories"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String, nullable=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=utcnow)
    subcategories = relationship("Subcategory", back_populates="category", cascade="all, delete-orphan")

class Subcategory(Base):
    __tablename__ = "subcategories"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(Text, nullable=True)
    category_id = Column(String, ForeignKey("categories.id"), nullable=False)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=utcnow)
    category = relationship("Category", back_populates="subcategories")

class PCPart(Base):
    __tablename__ = "pc_parts"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String)
    brand = Column(String, nullable=True)
    category = Column(String, index=True)
    category_id = Column(String, ForeignKey("categories.id"), nullable=True)
    subcategory_id = Column(String, ForeignKey("subcategories.id"), nullable=True)
    manufacturer = Column(String)
    model = Column(String)
    specs = Column(JSON, default=dict)
    price = Column(Float)
    power_consumption = Column(Integer, nullable=True)
    compatibility = Column(JSON, default=dict)
    image_url = Column(String, nullable=True)
    stock_status = Column(String, default="in_stock")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

class Build(Base):
    __tablename__ = "builds"
    id = Column(String, primary_key=True, default=gen_id)
    user_id = Column(String, ForeignKey('users.id'))
    name = Column(String)
    description = Column(Text, nullable=True)
    parts = Column(JSON, default=list)
    total_price = Column(Float, default=0)
    is_public = Column(Boolean, default=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(String, primary_key=True, default=gen_id)
    user_id = Column(String, ForeignKey('users.id'))
    product_id = Column(String, ForeignKey('products.id'))
    created_at = Column(DateTime, default=utcnow)

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(String, primary_key=True, default=gen_id)
    user_id = Column(String, ForeignKey('users.id'))
    type = Column(String)  # message, follow, like, comment, order, system
    title = Column(String)
    content = Column(Text, nullable=True)
    reference_id = Column(String, nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=utcnow)

class APIKey(Base):
    __tablename__ = "api_keys"
    id = Column(String, primary_key=True, default=gen_id)
    user_id = Column(String, ForeignKey('users.id'))
    key = Column(String, unique=True, index=True)
    name = Column(String, default="Default")
    is_active = Column(Boolean, default=True)
    last_used = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=utcnow)

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=gen_id)
    buyer_id = Column(String, ForeignKey('users.id'))
    seller_id = Column(String, ForeignKey('users.id'))
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)
    total_price = Column(Float)
    status = Column(String, default="pending")  # pending, confirmed, shipped, delivered, cancelled
    delivery_address = Column(Text, nullable=True)
    payment_method = Column(String, default="cash")
    is_paid = Column(Boolean, default=False)
    tracking_number = Column(String, nullable=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)
