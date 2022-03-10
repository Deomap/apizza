from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    is_active: bool = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True