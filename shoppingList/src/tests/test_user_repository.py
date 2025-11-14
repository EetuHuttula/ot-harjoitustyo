
import unittest
from repository import user_repository


class TestAddUser(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.username = "testuser"
        self.password = "testspass1"

    def test_add_user_success(self):
        result = user_repository.add_user(self.username, self.password)
        self.assertEqual(result, "User added successfully")

    def test_add_user_error(self):
        self.input_username = "testuser"
        self.input_password = "testspass1"
        result = user_repository.add_user(self.input_username, self.input_password)
        result = user_repository.add_user(self.input_username, self.input_password)
        self.assertEqual(result, "Username already exists")
    
    def test_add_user_invalid_input(self):
        self.username = ""
        self.password = ""
        result = user_repository.add_user(self.username, self.password)
        self.assertEqual(result,"Username and password are required")


 