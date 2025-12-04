"""Login view module for user login interface."""

from tkinter import ttk, StringVar, constants
from ui.base_view import BaseView


class LoginView(BaseView):
    """UI component for user login."""

    def __init__(self, root, register_handler, login_handler):
        """Initialize login view.

        Args:
            root: Parent Tk widget
            register_handler: Callback to navigate to registration view
            login_handler: Callback for login logic
        """
        super().__init__(root)
        self._register_handler = register_handler
        self._login_handler = login_handler
        self._username_entry = None
        self._password_entry = None
        self._initialize()

    def _login_handler_wrapper(self):
        """Handle login form submission."""
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._error("Username and password are required")
            return

        try:
            result = self._login_handler(username, password)
            if not result:
                self._error("Invalid username or password")
        except Exception as e:
            self._error(str(e))

    def _register_handler_wrapper(self):
        """Navigate to registration view."""
        self._register_handler()

    def _initialize(self):
        """Initialize the login view UI components."""
        self._frame = ttk.Frame(master=self._root)
        self._message_variable = StringVar(self._frame)

        message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message_variable,
            foreground="red"
        )
        message_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self._username_entry = self._create_form_field(1, "Username")
        self._password_entry = self._create_form_field(2, "Password", show_char="*")

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler_wrapper
        )
        register_button = ttk.Button(
            master=self._frame,
            text="Don't have an account? Register",
            command=self._register_handler_wrapper
        )
        login_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        register_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
