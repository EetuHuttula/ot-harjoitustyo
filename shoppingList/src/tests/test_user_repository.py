import unittest
from repository import user_repository


class TestAddUser(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all_users()
        self.username = "testuser"
        self.password = "testspass1"

    def tearDown(self):
        user_repository.delete_all_users()

    def test_add_user_success(self):
        user_repository.add_user(self.username, self.password)
        user = user_repository.get_user_by_username(self.username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)

    def test_add_user_error(self):
        user_repository.add_user(self.username, self.password)
        with self.assertRaises(Exception) as context:
            user_repository.add_user(self.username, self.password)
        self.assertIn("Username already exists", str(context.exception))

    def test_add_user_invalid_input(self):
        with self.assertRaises(Exception) as context:
            user_repository.add_user("", "")
        self.assertIn("Username and password are required",
                      str(context.exception))
        
    def test_verify_password_success(self):
        user_repository.add_user(self.username, self.password)
        result = user_repository.verify_password(self.username, self.password)
        self.assertTrue(result)

    def test_verify_password_failure(self):
        user_repository.add_user(self.username, self.password)
        result = user_repository.verify_password(self.username, "wrongpass")
        self.assertFalse(result)

    def test_verify_password_nonexistent_user(self):
        result = user_repository.verify_password("nonexistent", "somepass")
        self.assertFalse(result)
    