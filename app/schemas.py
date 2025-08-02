from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductRead(ProductCreate):
    id: int
    created_at: str
    class Config:
        orm_mode = True
