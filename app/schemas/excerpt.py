from pydantic import BaseModel
from typing import List, Optional

class ExcerptBase(BaseModel):
    image_url: Optional[str] = None
    text: str
    thoughts: Optional[str] = None

class ExcerptCreate(ExcerptBase):
    pass

class ExcerptOut(ExcerptBase):
    id: int

    class Config:
        orm_mode = True