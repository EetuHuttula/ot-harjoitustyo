""" Test module for testinh shopping repository. """

import unittest
from repository import shopping_repository

class TestShoppingRepository(unittest.TestCase):
    """Test cases for shopping repository functions."""
    
    def setUp(self):
        """Set up test fixtures before each test."""
        shopping_repository._save_raw([])
        self.username = "testuser"

    def tearDown(self):
        """Clean up after each test."""
        shopping_repository._save_raw([])

    def test_add_item_success(self):
        """Test successful addition of an item."""
        item_name = "Apples"
        amount = "2 kg"
        item = shopping_repository.add_item(item_name, amount, self.username)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, item_name)
        self.assertEqual(item.amount, amount)
        self.assertEqual(item.owner, self.username)
    
    def test_add_item_invalid_input(self):
        """Test error when adding item with empty inputs."""
        with self.assertRaises(Exception) as context:
            shopping_repository.add_item("", "", self.username)
        self.assertIn("Item name is required", str(context.exception))

    def test_list_items_by_owner(self):
        """Test listing items by owner."""
        shopping_repository.add_item("Eggs", "1", self.username)
        shopping_repository.add_item("Apples", "3", self.username)
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 2)
        item_names = [item.name for item in items]
        self.assertIn("Eggs", item_names)
        self.assertIn("Apples", item_names)

    def test_list_items_by_owner_no_items(self):
        """Test listing items for a user with no items."""
        items = shopping_repository.list_items_by_owner("nonexistentuser")
        self.assertEqual(len(items), 0)
    
    def test_clear_list(self):
        """Test clearing the shopping list for a user."""
        shopping_repository.add_item("Macarons", "500", self.username)
        shopping_repository.add_item("Beef", "1", self.username)
        shopping_repository.delete_all_items()
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 0)
    
    def test_clear_list_no_items(self):
        """Test clearing the shopping list for a user with no items."""
        shopping_repository.delete_all_items()
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 0)
    
    def test_remove_item(self):
        """Test removing a specific item from the shopping list."""
        item = shopping_repository.add_item("Bananas", "6", self.username)
        res = shopping_repository.remove_item(item.id, self.username)
        self.assertTrue(res)
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 0)

    def test_parse_numeric_value_int(self):
        """Test parsing integer values."""
        self.assertEqual(shopping_repository._parse_numeric_value("42"), 42)
        self.assertEqual(shopping_repository._parse_numeric_value("0"), 0)
        self.assertEqual(shopping_repository._parse_numeric_value("-10"), -10)

    def test_parse_numeric_value_float(self):
        """Test parsing float values."""
        self.assertEqual(shopping_repository._parse_numeric_value("3.14"), 3.14)
        self.assertEqual(shopping_repository._parse_numeric_value("0.5"), 0.5)
        self.assertEqual(shopping_repository._parse_numeric_value("-2.5"), -2.5)

    def test_parse_numeric_value_string(self):
        """Test parsing non-numeric strings returns None."""
        self.assertIsNone(shopping_repository._parse_numeric_value("abc"))
        self.assertIsNone(shopping_repository._parse_numeric_value("2 kg"))
        self.assertIsNone(shopping_repository._parse_numeric_value(""))

    def test_parse_numeric_value_none_and_type_errors(self):
        """Test parsing None and invalid types returns None."""
        self.assertIsNone(shopping_repository._parse_numeric_value(None))
        self.assertIsNone(shopping_repository._parse_numeric_value([]))
        self.assertIsNone(shopping_repository._parse_numeric_value({}))

    def test_update_existing_item_both_numeric_int(self):
        """Test updating item with two numeric int values."""
        rec = {"amount": "5"}
        shopping_repository._update_existing_item(rec, "3")
        self.assertEqual(rec["amount"], 8)

    def test_update_existing_item_both_numeric_float(self):
        """Test updating item with two numeric float values."""
        rec = {"amount": "2.5"}
        shopping_repository._update_existing_item(rec, "1.5")
        self.assertEqual(rec["amount"], 4.0)

    def test_update_existing_item_mixed_numeric(self):
        """Test updating item with int and float values."""
        rec = {"amount": "5"}
        shopping_repository._update_existing_item(rec, "2.5")
        self.assertEqual(rec["amount"], 7.5)

    def test_update_existing_item_one_non_numeric(self):
        """Test updating item when one value is non-numeric."""
        rec = {"amount": "2 kg"}
        shopping_repository._update_existing_item(rec, "5")
        self.assertEqual(rec["amount"], "5")

    def test_update_existing_item_both_non_numeric(self):
        """Test updating item when both values are non-numeric."""
        rec = {"amount": "2 kg"}
        shopping_repository._update_existing_item(rec, "3 kg")
        self.assertEqual(rec["amount"], "3 kg")

    def test_update_existing_item_float_result_as_int(self):
        """Test updating item where float result equals int."""
        rec = {"amount": "2.0"}
        shopping_repository._update_existing_item(rec, "3.0")
        self.assertEqual(rec["amount"], 5)
        self.assertIsInstance(rec["amount"], int)
    