"""Service layer for shopping list operations."""

from repository import shopping_repository


class ShoppingListService:
    """Handles shopping list logic for a user."""

    def get_shopping_list(self, username: str):
        """Return the shopping list for the given user (list of Shopping)."""
        if not username:
            return []
        return shopping_repository.list_items_by_owner(username)

    def add_item(self, username: str, item_name: str, quantity: str):
        """Add an item to the user's shopping list and return the created item."""
        if not username:
            raise ValueError("User must be provided")
        if not item_name:
            raise ValueError("Item name is required")
        if not quantity:
            quantity = "1"
        if not quantity.isdigit() or int(quantity) <= 0:
            raise ValueError("Quantity must be a positive integer")
        quantity = int(quantity)
        return shopping_repository.add_item(item_name, quantity, username)

    def remove_item(self, username: str, item_id: int):
        """Remove a specific item from the user's shopping list."""
        if not username:
            raise ValueError("User must be provided")
        if not shopping_repository.remove_item(item_id, username):
            raise ValueError("Item not found or does not belong to user")
        return True

    def clear_list(self, username: str):
        """Clear all items for the given user."""
        items = shopping_repository.load_all_items()
        remaining = [rec for rec in items
                     if rec.get("owner") != username]
        shopping_repository.save_all_items(remaining)
        return True


# AI GENERATED START
_service = ShoppingListService()


def get_shopping_list(username: str):
    """Get shopping list for a user."""
    return _service.get_shopping_list(username)


def add_item(username: str, item_name: str, quantity: str):
    """Add item to user's shopping list."""
    return _service.add_item(username, item_name, quantity)


def clear_list(username: str):
    """Clear all items for a user."""
    return _service.clear_list(username)

# AI GENERATED ENDS
