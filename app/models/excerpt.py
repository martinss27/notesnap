from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Excerpt(Base):
    __tablename__ = "excerpts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=True)
    thoughts = Column(String, nullable=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="excerpts")
    book = relationship("Book", back_populates="excerpts")