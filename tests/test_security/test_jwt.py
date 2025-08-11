import pytest
from jwt.exceptions import InvalidTokenError

from src.utils.security import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token


class TestJWT:
    def test_jwt_access_token(self):
        data = {"sub": "test"}
        token = create_access_token(data)

        assert token is not None

    def test_jwt_refresh_token(self):
        data = {"sub": "test"}
        token = create_refresh_token(data)

        assert token is not None

    def test_jwt_decode_access_token(self):
        data = {"sub": "test"}
        token = create_access_token(data)   

        decoded = decode_access_token(token)

        assert decoded is not None
        assert decoded["sub"] == data["sub"]

    def test_jwt_decode_refresh_token(self):
        data = {"sub": "test"}
        token = create_refresh_token(data)

        decoded = decode_refresh_token(token)

        assert decoded is not None
        assert decoded["sub"] == data["sub"]

    def test_jwt_decode_invalid_token(self):
        token = "invalid"

        with pytest.raises(InvalidTokenError):
            decode_access_token(token)
