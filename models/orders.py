from pydantic import BaseModel
from .products import Product


class OrderBase(BaseModel):
    type: str
    delivery_adds: int | None
    status: str
    products: list[Product]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# заказ: создать (оплата), обновить(трекинг), удалить, чтение(курьер, кухня)
