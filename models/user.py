from sqlalchemy import column, Integer, String
from database import Base

class User(Base):

    __tablename__ = "users"

    id = column(Integer, primary_key=True, index=True)
    email = column(String, unique=True, index=True, nullable=False)
    hashed_password = column(String, nullable=False)