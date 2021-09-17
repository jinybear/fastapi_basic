from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class AddUser(User):
    password: str

class UserInDB(User):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True

# class TokenData(BaseModel):
#     username: Optional[str] = None