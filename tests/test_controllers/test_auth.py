from fastapi.testclient import TestClient

from app import app


client = TestClient(app)

class TestAuth:
    email: str
    password: str
    refresh_token: str
    access_token: str

    @classmethod
    def setup_class(cls):
        cls.email = "testuser@gmail.com"
        cls.password = "megasuperduperpassword123!!"

    def test_register(self):
        response = client.post(
            "api/v1/auth/register", 
            json={"email": self.email, "password": self.password}
        )
        assert response.status_code in (200, 400)

    def test_refresh_token_with_invalid_password(self):
        response = client.post(
            "api/v1/auth/refresh_token", 
            json={"email": self.email, "password": "invalid_password"}
        )
        assert response.status_code == 401

    def test_refresh_token_with_invalid_email(self):
        response = client.post(
            "api/v1/auth/refresh_token", 
            json={"email": "invalid_email@gmail.com", "password": self.password}
        )
        assert response.status_code == 401

    def test_bad_email_format(self):
        response = client.post(
            "api/v1/auth/refresh_token", 
            json={"email": "invalid_email", "password": self.password}
        )
        assert response.status_code == 422

    def test_access_token(self):
        response = client.post(
            "api/v1/auth/refresh_token", 
            json={"email": self.email, "password": self.password}
        )
        assert response.status_code == 200
        refresh_token = response.json()["token"]
        assert refresh_token is not None and len(refresh_token) > 10

        response = client.post(
            "api/v1/auth/access_token", 
            json={"refresh_token": refresh_token}
        )
        assert response.status_code == 200
        access_token = response.json()["token"]
        assert access_token is not None

        response = client.get(
            "api/v1/user/me",
            headers={"token": access_token}
        )
        assert response.status_code == 200
        assert response.json() == self.email
            
