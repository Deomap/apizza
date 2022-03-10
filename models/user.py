from pydantic import BaseModel


class UserBase(BaseModel):
    is_guest: bool
    is_active: bool


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
