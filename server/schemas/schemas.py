"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

# ===== Auth Schemas =====
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AuthResponse(BaseModel):
    access_token: str
    user: 'UserResponse'

# ===== User Schemas =====
class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
    xp: int
    level: int
    badges: List[str]
    followers: int
    following: int
    role: str
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserProfile(BaseModel):
    id: str
    username: str
    avatar: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    website: Optional[str]
    xp: int
    level: int
    badges: List[str]
    posts_count: int
    followers: int
    following: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Product Schemas =====
class ProductCreate(BaseModel):
    title: str
    description: str
    price: float
    condition: str
    category: str
    images: List[str] = []
    location: str
    specs: dict = {}
    shipping_available: bool = True
    cash_on_delivery: bool = True
    crypto_payment: bool = False

class ProductUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    images: Optional[List[str]] = None

class ProductResponse(BaseModel):
    id: str
    title: str
    description: str
    price: float
    condition: str
    category: str
    images: List[str]
    seller_id: str
    location: str
    rating: float
    reviews_count: int
    views: int
    is_available: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Review Schemas =====
class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: str

class ReviewResponse(BaseModel):
    id: str
    product_id: str
    user_id: str
    rating: int
    comment: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Community Schemas =====
class CommunityCreate(BaseModel):
    name: str
    description: str
    icon: Optional[str] = None
    is_private: bool = False

class CommunityResponse(BaseModel):
    id: str
    name: str
    description: str
    icon: Optional[str]
    member_count: int
    owner_id: str
    is_private: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Post Schemas =====
class PostCreate(BaseModel):
    title: str
    content: str
    community_id: str
    images: List[str] = []

class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    community_id: str
    images: List[str]
    upvotes: int
    downvotes: int
    comments_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Comment Schemas =====
class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: str
    post_id: str
    author_id: str
    content: str
    upvotes: int
    downvotes: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== Message Schemas =====
class MessageCreate(BaseModel):
    receiver_id: str
    content: str

class MessageResponse(BaseModel):
    id: str
    sender_id: str
    receiver_id: str
    content: str
    is_read: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== PC Build Schemas =====
class BuildCreate(BaseModel):
    name: str
    description: Optional[str] = None
    cpu_id: Optional[str] = None
    gpu_id: Optional[str] = None
    ram_id: Optional[str] = None
    motherboard_id: Optional[str] = None
    psu_id: Optional[str] = None
    storage_id: Optional[str] = None
    case_id: Optional[str] = None
    is_public: bool = False

class BuildResponse(BaseModel):
    id: str
    user_id: str
    name: str
    description: Optional[str]
    total_price: float
    estimated_fps: Optional[int]
    bottleneck_info: Optional[str]
    is_public: bool
    likes: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ===== PC Part Schemas =====
class PCPartResponse(BaseModel):
    id: str
    name: str
    category: str
    manufacturer: str
    model: str
    specs: dict
    price: float
    power_consumption: Optional[int]
    
    class Config:
        from_attributes = True

# ===== Pagination =====
class PaginationParams(BaseModel):
    skip: int = 0
    limit: int = 20

class PaginatedResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: List[dict]
