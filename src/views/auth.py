from fastapi import APIRouter

from src.dto import RefreshTokenRequest, TokenResponse, RegisterRequest, AccessTokenRequest
from src.controllers.user import AuthController

auth_router = APIRouter(
    prefix="/auth"
)

@auth_router.post("/refresh_token")
async def refresh_token(auth_data: RefreshTokenRequest) -> TokenResponse:
    """Create new refresh token
    """
    return await AuthController.refresh_token(auth_data=auth_data)

@auth_router.post("/access_token")
async def access_token(auth_data: AccessTokenRequest) -> TokenResponse:
    """Create new access token  
    """
    return await AuthController.access_token(auth_data=auth_data)

@auth_router.post("/register")
async def register(auth_data: RegisterRequest) -> int:
    """Register new user
    """
    return await AuthController.register(auth_data=auth_data)
