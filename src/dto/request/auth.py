from pydantic import BaseModel, Field, EmailStr


class RefreshTokenRequest(BaseModel):
    email: EmailStr
    password: str = Field(max_length=128)


class AccessTokenRequest(BaseModel):
    refresh_token: str = Field(min_length=10)

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(max_length=128)
