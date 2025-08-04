from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    description = Column(Text)
#    user_id = Column(Integer,nullable=False)

    excerpts = relationship("Excerpt", back_populates="book", cascade="all, delete-orphan")