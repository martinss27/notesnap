from pydantic import BaseModel
from typing import List, Optional

class ChapterBase(BaseModel):
    title: str

class ChapterCreate(ChapterBase):
    pass

class ChapterOut(ChapterBase):
    id: int

    class Config:
        orm_mode = True