from pydantic import BaseModel


class UserBase(BaseModel):
    type: str | None
    forename: str| None
    email: str| None


class UserInAuth(UserBase):
    hashed_password: bytes | None
    salt: bytes | None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
