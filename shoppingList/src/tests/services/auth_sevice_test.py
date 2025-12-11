import unittest
from services.auth_service import login_handler, register_handler
from repository.user_repository import UserAlreadyExistsError, InvalidUserDataError


class TestRegisterHandler(unittest.TestCase):

    def setUp(self):
        from repository import user_repository
        user_repository.delete_all_users()
        self.username = "newuser"
        self.password = "newpass1"

    def tearDown(self):
        """Clean up after each test."""
        from repository import user_repository
        user_repository.delete_all_users()

    def test_register_success(self):
        try:
            register_handler(None, self.username, self.password)
        except Exception as e:
            self.fail(
                f"register_handler raised an exception unexpectedly: {e}")

    def test_register_existing_username(self):
        register_handler(None, self.username, self.password)
        with self.assertRaises(UserAlreadyExistsError) as context:
            register_handler(None, self.username, self.password)
        self.assertIn("Username already exists", str(context.exception))

    def test_login_success(self):
        register_handler(None, self.username, self.password)
        try:
            result = login_handler(None, self.username, self.password)
            self.assertTrue(result)
        except Exception as e:
            self.fail(f"login_handler raised an exception unexpectedly: {e}")

    def test_login_invalid_credentials(self):
        register_handler(None, self.username, self.password)
        result = login_handler(None, self.username, "wrongpass")
        self.assertFalse(result)

    def test_login_without_credentials(self):
        result = login_handler(None)
        self.assertIsNone(result)

    def test_login_with_credentials_and_callback(self):
        register_handler(None, self.username, self.password)

        callback_username = None

        def on_success(username):
            nonlocal callback_username
            callback_username = username

        result = login_handler(None, self.username, self.password, on_success)
        self.assertTrue(result)
        self.assertEqual(callback_username, self.username)

    def test_login_invalid_credentials_with_callback(self):
        register_handler(None, self.username, self.password)

        callback_called = False

        def on_success(username):
            nonlocal callback_called
            callback_called = True

        result = login_handler(None, self.username, "wrongpass", on_success)
        self.assertFalse(result)
        self.assertFalse(callback_called)