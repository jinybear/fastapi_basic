from fastapi import Depends, APIRouter
from controllers.models.auth import AddUser

from services.auth import oauth2_scheme
from services.test import (service_calculate_profit,
                           service_add_user,
                           service_read_user_me)
from controllers.models.auth import User, UserInDB

router = APIRouter(tags=['test'], dependencies=[Depends(oauth2_scheme)])


@router.get("/users/me/", response_model=UserInDB)
async def read_users_me(result: str = Depends(service_read_user_me)):
    return result

@router.post("/calculate_profit")
async def calculate_profit(result: dict = Depends(service_calculate_profit)):
    return result

@router.post("/users/add", status_code=201)
async def add_user(result: str = Depends(service_add_user)):
    return result

