from pydantic import BaseModel
from typing import List, Optional
from app.schemas.chapter import ChapterOut

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class BookCreate(BookBase):
    user_id: int

class BookOut(BookBase):
    id: int
    chapters: List[ChapterOut] = []

    class Config:
        orm_mode = True