from pydantic import BaseModel
from typing import Optional


class OrderBase(BaseModel):
    type: str
    delivery_adds: Optional[int]
    status: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# заказ: создать (оплата), обновить(трекинг), удалить, чтение(курьер, кухня)
