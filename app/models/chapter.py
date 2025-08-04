from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    book = relationship("Book", back_populates="chapters")
    excerpts = relationship("Excerpt", back_populates="chapter", cascade="all, delete-orphan")