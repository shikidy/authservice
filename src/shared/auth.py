from typing import Annotated
import jwt

from fastapi import Header
from fastapi.exceptions import HTTPException

from src.models.user import UserModel
from src.utils.security import decode_access_token


async def get_current_user(authorization: Annotated[str | None, Header(alias="token")]) -> UserModel:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        decoded_refresh_token = decode_access_token(authorization)
    except (jwt.DecodeError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    user = await UserModel.get(id_=int(decoded_refresh_token["sub"]))
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user