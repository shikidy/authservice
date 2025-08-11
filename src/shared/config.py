from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_url: str
    rtoken_secret: str
    rtoken_expire_d: int
    atoken_secret: str
    a_token_expire_m: int
    algorithm: str
    cors_host: str = Field(alias="corshost")
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_config() -> Config:
    return Config() # type:
