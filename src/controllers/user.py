
from fastapi import HTTPException
import jwt

from src.dto import RefreshTokenRequest, TokenResponse, RegisterRequest, AccessTokenRequest
from src.models.user import UserModel
from src.utils.security import verify_password, create_refresh_token, hash_password, decode_refresh_token, create_access_token


class AuthController:


    @staticmethod
    async def refresh_token(auth_data: RefreshTokenRequest) -> TokenResponse:
        user = await UserModel.get(email=auth_data.email)
        if user is None or not verify_password(auth_data.password, user.password_hash):
            raise HTTPException(401, detail="Invalid credentials")
        try:
            refresh_token = create_refresh_token(data={"sub": str(user.id)})
        except (jwt.DecodeError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise HTTPException(401, detail="Invalid credentials")
        return TokenResponse(token=refresh_token)
        
    @staticmethod
    async def register(auth_data: RegisterRequest) -> int:
        user = await UserModel.get(email=auth_data.email)
        if user is not None:
            raise HTTPException(400, detail="User already exists")
        user = await UserModel.create(email=auth_data.email, password_hash=hash_password(auth_data.password))
        return 200
    
    @staticmethod
    async def access_token(auth_data: AccessTokenRequest) -> TokenResponse:
        try:
            decoded_refresh_token = decode_refresh_token(auth_data.refresh_token)
        except (jwt.DecodeError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise HTTPException(401, detail="Invalid credentials")
        user = await UserModel.get(id_=int(decoded_refresh_token["sub"]))
        if user is None:
            raise HTTPException(401, detail="Invalid credentials")
        access_token = create_access_token(data={"sub": str(user.id)})
        return TokenResponse(token=access_token)
