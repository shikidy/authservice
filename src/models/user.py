from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .base import Base, async_session_maker


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now()) #pylint: disable=e1102

    @staticmethod
    async def get(
        *,
        id_: Optional[int] = None,
        email: Optional[str] = None,
    ) -> Optional["UserModel"]:
        stmt = select(UserModel)
        if id_ is not None:
            stmt = stmt.where(UserModel.id == id_)
        if email is not None:
            stmt = stmt.where(UserModel.email == email)
        async with async_session_maker() as session:
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
    
    @staticmethod
    async def create(
        *,
        email: str,
        password_hash: str,
    ) -> "UserModel":
        user = UserModel(email=email, password_hash=password_hash)
        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
