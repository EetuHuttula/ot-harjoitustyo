import unittest
from repository import shopping_repository

class TestShoppingRepository(unittest.TestCase):


    def setUp(self):
        shopping_repository._save_raw([])
        self.username = "testuser"

    def tearDown(self):
        shopping_repository._save_raw([])

    def test_add_item_success(self):
        item_name = "Apples"
        amount = "2 kg"
        item = shopping_repository.add_item(item_name, amount, self.username)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, item_name)
        self.assertEqual(item.amount, amount)
        self.assertEqual(item.owner, self.username)
    
    def test_add_item_invalid_input(self):
        with self.assertRaises(Exception) as context:
            shopping_repository.add_item("", "", self.username)
        self.assertIn("Item name is required", str(context.exception))

    def test_list_items_by_owner(self):
        shopping_repository.add_item("Eggs", "1", self.username)
        shopping_repository.add_item("Apples", "3", self.username)
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 2)
        item_names = [item.name for item in items]
        self.assertIn("Eggs", item_names)
        self.assertIn("Apples", item_names)

    def test_list_items_by_owner_no_items(self):

        items = shopping_repository.list_items_by_owner("nonexistentuser")
        self.assertEqual(len(items), 0)
    
    def test_clear_list(self):
        shopping_repository.add_item("Macarons", "500", self.username)
        shopping_repository.add_item("Beef", "1", self.username)
        shopping_repository.delete_all_items()
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 0)
    
    def test_remove_item(self):
        item = shopping_repository.add_item("Bananas", "6", self.username)
        res = shopping_repository.remove_item(item.id, self.username)
        self.assertTrue(res)
        items = shopping_repository.list_items_by_owner(self.username)
        self.assertEqual(len(items), 0)

    def test_update_existing_item_both_numeric_int(self):
        rec = {"amount": "5"}
        shopping_repository._update_existing_item(rec, "3")
        self.assertEqual(rec["amount"], 8)

    def test_update_existing_item_both_numeric_float(self):
        rec = {"amount": "2.5"}
        shopping_repository._update_existing_item(rec, "1.5")
        self.assertEqual(rec["amount"], 4.0)