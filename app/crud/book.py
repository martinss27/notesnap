from sqlalchemy.orm import Session
from app.models.book import Book

def create_book(db: Session, book_data, user_id: int):
    db_book = Book(
        title=book_data.title,
        author=book_data.author,
        description=book_data.description,
        user_id=user_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, user_id: int):
    return db.query(Book).filter(Book.user_id == user_id).all()