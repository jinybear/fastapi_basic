from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from jose import JWTError, jwt

from services.auth import oauth2_scheme
from controllers.models.auth import AddUser, UserInDB
from controllers.models.test import Calculate_Data
import models

from config import oper_settings

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, oper_settings.setting['token']['SECRET_KEY'],
                             algorithms=oper_settings.setting['token']['ALGORITHM'])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception

def service_read_user_me(username: str = Depends(get_current_user), db: models.SessionLocal = Depends(models.get_db)):
    try:
        user = db.query(models.user.User).filter(models.user.User.username == username).first()
        return UserInDB.from_orm(user)
    except Exception as ex:
        print(ex)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

def service_calculate_profit(cal_data: Calculate_Data):
    print("inputed money :", cal_data.money, end=", ")
    print("inputed years :", cal_data.years, end=", ")
    print("inputed profit :", cal_data.profit)
    result = cal_data.money

    for year in range(1, int(cal_data.years) + 1):
        result += result * cal_data.profit
        print(f"After {year} year: {result}")
        result += cal_data.add_money_per_year

    return {"result": int(result - cal_data.add_money_per_year)}

def service_add_user(add_user: AddUser, db: models.SessionLocal = Depends(models.get_db)):
    try:
        db.add(
            models.user.User(username=add_user.username,
                        full_name=add_user.full_name, email=add_user.email,
                        hashed_password=add_user.password)
            )
        return {'result': 'Success', 'msg': ''}
    except Exception as ex:
        raise ex