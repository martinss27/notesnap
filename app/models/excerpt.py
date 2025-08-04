from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Excerpt(Base):
    __tablename__ = "excerpts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    thoughts = Column(Text, nullable=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    book = relationship("Book", back_populates="excerpts")