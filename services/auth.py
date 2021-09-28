from datetime import datetime, timedelta
from fastapi import HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from jose import jwt

from app import settings
from controllers.models.auth import UserInDB
from models import SessionLocal
from models.user import User

# to get a string like this run:
# openssl rand -hex 32

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     },
#     "johndoe2": {
#         "username": "johndoe2",
#         "full_name": "John Doe2",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2a$12$kPQoUWlMWId8cBYLyxkCxeCUrfZ38Zy9lOutlxxiKwYfTweofgOje",
#         "disabled": False,
#     }
# }

class Service_auth():
    def __get_user(self, username: str):
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()

        user_data = UserInDB.from_orm(user)
        return user_data

        # if username in fake_users_db:
        #     user_dict = fake_users_db[username]
        #     return UserInDB(**user_dict)

    def __authenticate_user(self, username: str, password: str):
        user = self.__get_user(username)
        if not user:
            return False
        if not pwd_context.verify(password, user.hashed_password):
            return False
        return user

    def __create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def gen_token(self, username, password):
        user = self.__authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return access_token

service_auth = Service_auth()