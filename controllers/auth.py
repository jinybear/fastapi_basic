from fastapi import Depends, APIRouter, Response
from fastapi.security import OAuth2PasswordRequestForm

from controllers.models.auth import Token, UserInDB
from services.auth import service_auth

router = APIRouter(tags=['token'])

@router.post("/token", response_model=Token)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = service_auth.gen_token(form_data.username, form_data.password)

    response.set_cookie(key='access_token', value=access_token)
    return {"access_token": access_token, "token_type": "bearer"}

