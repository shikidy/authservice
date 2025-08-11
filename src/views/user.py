from typing import Annotated

from fastapi import APIRouter, Depends

from src.shared.auth import get_current_user

from src.models.user import UserModel


user_router = APIRouter(
    prefix="/user"
)

@user_router.get("/me")
async def get_me(user: Annotated[UserModel, Depends(get_current_user)]) -> str:
    """Get current user
    """
    return user.email
