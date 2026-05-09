from sqlalchemy.orm import Session
from models.models import User
from utils.auth import hash_password, verify_password, create_access_token
from utils.helpers import generate_id, validate_username, calculate_level

class AuthService:
    @staticmethod
    def register(db: Session, username: str, email: str, password: str) -> User:
        if not validate_username(username):
            raise ValueError("Invalid username")
        existing = db.query(User).filter(
            (User.email == email) | (User.username == username)
        ).first()
        if existing:
            raise ValueError("User already exists")
        user = User(id=generate_id(), username=username, email=email,
                    hashed_password=hash_password(password), xp=0, level=1)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def login(db: Session, email: str, password: str) -> tuple:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")
        token = create_access_token({"sub": user.id})
        return user, token

    @staticmethod
    def get_user_by_id(db: Session, user_id: str):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def add_xp(db: Session, user_id: str, xp: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        user.xp += xp
        user.level = calculate_level(user.xp)
        db.commit()
        db.refresh(user)
        return user
