from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    order_id: int | None

    class Config:
        orm_mode = True
