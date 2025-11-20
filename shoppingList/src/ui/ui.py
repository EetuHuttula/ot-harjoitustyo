"""UI module for managing application views."""

from ui.register_view import RegisterView
from ui.login_view import LoginView
from repository.user_repository import add_user
from services.auth_service import login_handler, register_handler


class UI:
    #AI generated starts
    def _main_view(self, username=None):
        """Display the main shopping list view. Placeholder implementation."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass
        from tkinter import ttk
        frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=frame, text=f"Welcome, {username}!")
        label.pack(padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        self.current_view = frame
    #AI generated ends
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
        self._login_view()

    def _login_view(self):
        """Display the login view."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass

        from services.auth_service import login_handler
        self.current_view = LoginView(
            self._root,
            self._register_view,
            lambda username, password: login_handler(
                self, username, password, self._main_view)
        )
        self.current_view.pack()

    def _register_view(self):
        """Display the registration view."""
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass

        from services.auth_service import register_handler
        self.current_view = RegisterView(
            self._root,
            lambda username, password: register_handler(
                self, username, password),
            self._login_view
        )
        self.current_view.pack()
