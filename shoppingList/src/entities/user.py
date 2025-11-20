"""User entity module."""


class User:
    """Represents a user in the shopping list application."""

    def __init__(self, username, password):
        """Initialize a new user with username and password.

        Args:
            username: The user's username
            password: The user's password
        """
        self.username = username
        self.password = password
