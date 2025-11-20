"""Test module for user repository."""

import unittest
from repository import user_repository


class TestAddUser(unittest.TestCase):
    """Test cases for user repository add_user function."""

    def setUp(self):
        """Set up test fixtures before each test."""
        user_repository.delete_all_users()
        self.username = "testuser"
        self.password = "testspass1"

    def tearDown(self):
        """Clean up after each test."""
        user_repository.delete_all_users()

    def test_add_user_success(self):
        """Test successful user addition."""
        user_repository.add_user(self.username, self.password)
        user = user_repository.get_user_by_username(self.username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)

    def test_add_user_error(self):
        """Test error when adding duplicate username."""
        user_repository.add_user(self.username, self.password)
        with self.assertRaises(Exception) as context:
            user_repository.add_user(self.username, self.password)
        self.assertIn("Username already exists", str(context.exception))

    def test_add_user_invalid_input(self):
        """Test error when adding user with empty inputs."""
        with self.assertRaises(Exception) as context:
            user_repository.add_user("", "")
        self.assertIn("Username and password are required",
                      str(context.exception))
