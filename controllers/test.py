from fastapi import Depends, APIRouter
from pydantic import BaseModel
from typing import Optional

from controllers.token import oauth2_scheme, check_token, get_user
from services.test import service_calculate_profit


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


router = APIRouter(tags=['test'], dependencies=[Depends(oauth2_scheme)])

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return check_token(token)

@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return get_user(current_user)

@router.post("/calculate_profit")
async def calculate_profit(result: dict = Depends(service_calculate_profit)):
    return result


