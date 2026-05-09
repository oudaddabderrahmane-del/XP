"""
Utility functions and helpers
"""

import uuid
from typing import Optional

def generate_id() -> str:
    """Generate a unique ID"""
    return str(uuid.uuid4())

def generate_short_id() -> str:
    """Generate a short unique ID"""
    return uuid.uuid4().hex[:12]

def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_username(username: str) -> bool:
    """Validate username format"""
    if len(username) < 3 or len(username) > 30:
        return False
    import re
    pattern = r'^[a-zA-Z0-9_-]+$'
    return re.match(pattern, username) is not None

def get_pagination_params(skip: int = 0, limit: int = 20) -> tuple:
    """Validate and return pagination parameters"""
    skip = max(0, skip)
    limit = min(100, max(1, limit))
    return skip, limit

def calculate_level(xp: int) -> int:
    """Calculate user level from XP"""
    # Each level requires progressively more XP
    # Level 1: 0 XP, Level 2: 100 XP, Level 3: 300 XP, etc.
    level = 1
    current_xp = 0
    xp_per_level = 100
    
    while current_xp + xp_per_level <= xp:
        current_xp += xp_per_level
        level += 1
        xp_per_level += 50
    
    return level
