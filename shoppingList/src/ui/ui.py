"""UI module for managing application views."""

from ui.register_view import RegisterView
from ui.login_view import LoginView
from ui.shopping_view import ShoppingView
from repository.user_repository import add_user
from services.auth_service import login_handler, register_handler


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
        """Start the UI with the login view."""
        self._login_view()

    def _destroy_current_view(self):
        """Destroy the current view safely."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass

    def _login_view(self):
        """Display the login view."""
        self._destroy_current_view()

        from services.auth_service import login_handler
        self.current_view = LoginView(
            self._root,
            self._register_view,
            lambda username, password: login_handler(
                self, username, password, self._shopping_view)
        )
        self.current_view.pack()

    def _shopping_view(self, username):
        """Display the shopping list view for the given username."""
        self._destroy_current_view()

        self.current_view = ShoppingView(
            self._root,
            username,
            self._login_view
        )
        self.current_view.pack()

    def _register_view(self):
        """Display the registration view."""
        self._destroy_current_view()

        from services.auth_service import register_handler
        self.current_view = RegisterView(
            self._root,
            lambda username, password: register_handler(
                self, username, password),
            self._login_view
        )
        self.current_view.pack()
