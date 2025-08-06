from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.database import SessionLocal
from app.crud.user import create_user, get_user_by_email, authenticate_user
from app.auth.jwt import create_access_token
from dotenv import load_dotenv
load_dotenv()
import os

SECRET_KEY = "qoGq3hMf4tfQg6toDS6sSy4tXyUeakvELSLHBG8qre4" # i put this here because it is not working with the .env file
ALGORITHM = "HS256"

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
        access_token: str = Cookie(None),
        db: Session = Depends(get_db)
):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")
    user = get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    new_user = create_user(db, user.email, user.password)
    return new_user

@router.post("/login")
def login(response: Response, user_in: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email,user_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"message": "login successful"}