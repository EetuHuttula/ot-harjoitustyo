"""UI module for managing application views."""

from ui.register_view import RegisterView
from ui.login_view import LoginView
from repository.user_repository import add_user
from services.auth_service import _login_handler, _register_handler

class UI:
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

        self.current_view = LoginView(
            self._root,
            self._register_view,
            lambda u, p: self._login_handler(u, p, self._main_view)
        )
        self.current_view.pack()

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

