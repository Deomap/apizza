from pydantic import BaseModel


class UserBase(BaseModel):
    type: str | None
    forename: str | None
    email: str | None


class UserInAuth(UserBase):
    hashed_password: str | None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# JWT
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
