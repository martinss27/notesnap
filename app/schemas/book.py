from pydantic import BaseModel
from typing import List, Optional

class ExcerptBase(BaseModel):
    text: str
    thoughts: Optional[str] = None

class ExcerptCreate(ExcerptBase):
    pass

class ExcerptOut(ExcerptBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class BookCreate(BookBase):
    excerpts: List[ExcerptCreate] = []

class BookOut(BookBase):
    id: int
    excerpts: List[ExcerptOut] = []

    class Config:
        orm_mode = True