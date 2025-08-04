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