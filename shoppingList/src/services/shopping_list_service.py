"""Service layer for shopping list operations."""

class ShoppingListService:
    """Handles shopping list logic for a user."""

    def __init__(self, user_repository):
        self._user_repository = user_repository


    def get_shopping_list(self, username):
        """Return the shopping list for the given user."""
        user = self._user_repository.get_user_by_username(username)
        if not user:
            return []

        return []

    def add_item(self, username, item_name, quantity):
        """Add an item to the user's shopping list."""
        pass

    def remove_item(self, username, item_name):
        """Remove an item from the user's shopping list."""
        pass

    def clear_list(self, username):
        """Clear the user's shopping list."""
        pass
