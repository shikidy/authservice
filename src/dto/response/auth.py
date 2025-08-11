from datetime import datetime
from pydantic import BaseModel


class TokenResponse(BaseModel):
    token: str
    # expired_at: datetime
