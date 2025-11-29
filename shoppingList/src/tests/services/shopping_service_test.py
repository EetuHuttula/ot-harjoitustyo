"""Concise tests for shopping list service wrapper functions."""

import unittest
from services import shopping_list_service


class TestShoppingService(unittest.TestCase):
    def setUp(self):
        self.user = "svc_user"
        shopping_list_service.clear_list(self.user)

    def tearDown(self):
        shopping_list_service.clear_list(self.user)

    def test_add_and_list(self):
        a = shopping_list_service.add_item(self.user, "chips", "1")
        self.assertEqual(a.name, "chips")
        items = shopping_list_service.get_shopping_list(self.user)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "chips")
    
    def test_add_item_when_no_username(self):
        with self.assertRaises(ValueError) as context:
            shopping_list_service.add_item("", "pepsi", "1")
        self.assertIn("User must be provided", str(context.exception))

    def test_error_getting_shopping_list_no_username(self):
        items = shopping_list_service.get_shopping_list("")
        self.assertEqual(len(items), 0)

    def test_clear_list(self):
        shopping_list_service.add_item(self.user, "Bebis", "1")
        shopping_list_service.add_item(self.user, "Coke", "1")
        shopping_list_service.clear_list(self.user)
        self.assertEqual(len(shopping_list_service.get_shopping_list(self.user)), 0)
