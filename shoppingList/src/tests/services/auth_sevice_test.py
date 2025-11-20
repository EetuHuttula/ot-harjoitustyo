import unittest
from services.auth_service import login_handler, register_handler
from repository.user_repository import UserAlreadyExistsError, InvalidUserDataError


class TestRegisterHandler(unittest.TestCase):
    """Test cases for auth_service register_handler function."""

    def setUp(self):
        """Set up test fixtures before each test."""
        from repository import user_repository
        user_repository.delete_all_users()
        self.username = "newuser"
        self.password = "newpass1"

    def tearDown(self):
        """Clean up after each test."""
        from repository import user_repository
        user_repository.delete_all_users()

    def test_register_success(self):
        """Test successful user registration."""
        try:
            register_handler(None, self.username, self.password)
        except Exception as e:
            self.fail(
                f"register_handler raised an exception unexpectedly: {e}")

    def test_register_existing_username(self):
        """Test error when registering with an existing username."""
        register_handler(None, self.username, self.password)
        with self.assertRaises(UserAlreadyExistsError) as context:
            register_handler(None, self.username, self.password)
        self.assertIn("Username already exists", str(context.exception))

    def test_login_success(self):
        """Test successful user login after registration."""
        register_handler(None, self.username, self.password)
        try:
            result = login_handler(None, self.username, self.password)
            self.assertTrue(result)
        except Exception as e:
            self.fail(f"login_handler raised an exception unexpectedly: {e}")

    def test_login_invalid_credentials(self):
        """Test error when logging in with invalid credentials."""
        register_handler(None, self.username, self.password)
        result = login_handler(None, self.username, "wrongpass")
        self.assertFalse(result)