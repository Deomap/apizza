from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    order_id: Optional[int]

    class Config:
        orm_mode = True
