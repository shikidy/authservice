import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext # type: ignore

from src.shared.config import get_config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password with hash

    Args:
        plain_password (str): raw password
        hashed_password (str): bcrypt hashed password

    Returns:
        bool: is verified
    """
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(plain_password: str) -> str:
    """Bcrypt hash password

    Args:
        plain_password (str): raw password

    Returns:
        str: hashed password
    """
    return pwd_context.hash(plain_password)

def create_token(data: dict, expires_delta: timedelta, secret: str, algo: str):
    """Create a JWT token

    Args:
        data (dict): data to encode
        expires_delta (timedelta): expiration time
        secret (str): secret key
        algo (str): algorithm
    """
    to_encode = data.copy()
    expire_at = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire_at})

    return jwt.encode(to_encode, secret, algorithm=algo)

def create_access_token(data: dict) -> str:
    """Create an access token

    Args:
        data (dict): data to encode

    Returns:
        str: access token
    """
    config = get_config()
    time_expires = timedelta(minutes=config.a_token_expire_m)
    return create_token(
        data,
        time_expires,
        config.atoken_secret,
        config.algorithm
    )

def create_refresh_token(data: dict) -> str:
    """Create a refresh token

    Args:
        data (dict): data to encode

    Returns:
        str: refresh token
    """
    config = get_config()
    time_expires = timedelta(days=config.rtoken_expire_d)
    return create_token(
        data,
        time_expires,
        config.rtoken_secret,
        config.algorithm
    )

def decode_token(token: str, secret: str, algo: str) -> dict:
    """Decode a JWT token

    Args:
        token (str): token to decode
        secret (str): secret key
        algo (str): algorithm
    """
    return jwt.decode(token, secret, algorithms=[algo])

def decode_access_token(token: str) -> dict:
    """Decode an access token

    Args:
        token (str): token to decode

    Returns:
        dict: decoded token
    """
    config = get_config()
    return decode_token(token, config.atoken_secret, config.algorithm)

def decode_refresh_token(token: str) -> dict:
    """Decode a refresh token

    Args:
        token (str): token to decode

    Returns:
        dict: decoded token
    """
    config = get_config()
    return decode_token(token, config.rtoken_secret, config.algorithm)
