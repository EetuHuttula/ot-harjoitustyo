"""UI module for managing application views."""

from ui.register_view import RegisterView
from repository.user_repository import add_user


class UI:
    """Main UI controller for the shopping list application."""

    def __init__(self, root):
        """Initialize the UI controller.

        Args:
            root: The root Tk widget
        """
        self._root = root
        self.current_view = None

    def start(self):
        """Start the UI with the registration view."""
        self._register_view()

    def _register_view(self):
        """Display the registration view."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass

        self.current_view = RegisterView(
            self._root,
            self._register_handler,
            self._login_handler
        )
        self.current_view.pack()

    def _register_handler(self, username, password):
        """Handle user registration.

        Args:
            username: The username to register
            password: The password for the user
        """
        add_user(username, password)
        try:
            message_var = self.current_view._message_variable
            message_var.set("Registered successfully")
        except Exception:
            pass

    def _login_handler(self):
        """Handle login view request."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass
