from src.utils.security import verify_password, hash_password


class TestHashes():

    def test_verify(self):
        plain_password = "somepassword123!!"

        hashed_password = hash_password(plain_password)

        assert verify_password(plain_password, hashed_password), "error on verify same password"

    def test_verify_invalid(self):
        plain_password = "somepassword123!we"
        second_password = "secondsomepassword123!"

        hashed_password = hash_password(plain_password)

        assert verify_password(second_password, hashed_password) is False, "invalid password verified as valid"
