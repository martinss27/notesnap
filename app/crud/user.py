from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.security import hash_password

def create_user(db: Session, email: str, password: str) -> User:
    hashed_pw = hash_password(password)
    db_user = User(email=email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db:Session, email: str):
    return db.query(User).filter(User.email == email).first()