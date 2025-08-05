from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut
from app.crud.book import create_book, get_books
from app.routers.auth import get_db

router = APIRouter()

# def get_current_user_id():

@router.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book, user_id)

@router.get("/books", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return get_books(db, user_id)