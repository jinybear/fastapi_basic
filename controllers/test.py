from fastapi import Depends, APIRouter
from pydantic import BaseModel
from typing import Optional

import models.user
from controllers.token import oauth2_scheme, check_token, get_user
from services.test import service_calculate_profit
from models import SessionLocal
from controllers.models.auth import User, UserInDB


router = APIRouter(tags=['test'], dependencies=[Depends(oauth2_scheme)])

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return check_token(token)

@router.get("/users/me/", response_model=UserInDB)
async def read_users_me(username: str = Depends(get_current_user)):
    db = SessionLocal()
    user = db.query(models.user.User).filter(models.user.User.username == username).first()
    return UserInDB.from_orm(user)

@router.post("/calculate_profit")
async def calculate_profit(result: dict = Depends(service_calculate_profit)):
    return result

