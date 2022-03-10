from pydantic import BaseModel
from .products import OrderProduct


class OrderBase(BaseModel):
    type: str
    delivery_adds: int | None
    status: str
    products: list[OrderProduct]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
