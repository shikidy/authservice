from dotenv import load_dotenv  # type: ignore
from sqlalchemy.orm import DeclarativeBase  # type: ignore
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine  # type: ignore
from sqlalchemy.pool import NullPool  # type: ignore

from src.shared.config import get_config


load_dotenv(override=False)
config = get_config()
DB_URL = config.db_url


engine = create_async_engine(DB_URL, echo=False, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, autoflush=True)

class Base(DeclarativeBase):
    ...
