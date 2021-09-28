from fastapi import Depends, HTTPException, status, APIRouter
from controllers.models.auth import AddUser
from jose import JWTError, jwt

import models.user
from services.auth import oauth2_scheme
from services.test import service_calculate_profit
from models import SessionLocal, get_db
from controllers.models.auth import User, UserInDB
from app import settings

router = APIRouter(tags=['test'], dependencies=[Depends(oauth2_scheme)])

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception

@router.get("/users/me/", response_model=UserInDB)
async def read_users_me(username: str = Depends(get_current_user)):
    db = SessionLocal()
    user = db.query(models.user.User).filter(models.user.User.username == username).first()
    return UserInDB.from_orm(user)

@router.post("/calculate_profit")
async def calculate_profit(result: dict = Depends(service_calculate_profit)):
    return result

@router.post("/users/add", status_code=201)
async def add_user(add_user: AddUser, db: SessionLocal = Depends(get_db)):
    try:
        db.add(
            models.user.User(username=add_user.username,
                        full_name=add_user.full_name, email=add_user.email,
                        hashed_password=add_user.password)
            )
        return {'result': 'Success', 'msg': ''}
    except Exception as ex:
        print(ex)
        return {'result':'Failed', 'msg':str(ex)}

