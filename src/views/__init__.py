from fastapi import APIRouter

from .auth import auth_router
from .user import user_router

api_router = APIRouter(
    prefix="/api/v1"
)

api_router.include_router(auth_router)
api_router.include_router(user_router)
