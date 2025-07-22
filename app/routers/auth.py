from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.database import SessionLocal
from app.crud.user import create_user, get_user_by_email, authenticate_user
from app.auth.jwt import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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