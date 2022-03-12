from pydantic import BaseModel
from .product import PizzeriaProduct


class PizzeriaBase(BaseModel):
    is_open: bool | None
    is_delivery_avbl: bool | None
    products: list[PizzeriaProduct] | None


class PizzeriaCreate(PizzeriaBase):
    pass


class Pizzeria(PizzeriaBase):
    id: int

    class Config:
        orm_mode = True
