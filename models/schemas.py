from pydantic import BaseModel
from typing import Optional


# ORDER
class OrderBase(BaseModel):
    type: str
    delivery_adds: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# заказ: создать (оплата), обновить(трекинг), удалить, чтение(курьер, кухня)


# USER
class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass

    class Config:
        orm_mode = True


# PRODUCT
class ProductBase(BaseModel):
    pass


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    pass

    class Config:
        orm_mode = True
