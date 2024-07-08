from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float


class ItemRead(ItemCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode =True