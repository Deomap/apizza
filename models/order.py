from pydantic import BaseModel
from .product import OrderProduct


class OrderBase(BaseModel):
    type: str
    delivery_adds: str | None
    status: str
    products: list[OrderProduct]
    price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
