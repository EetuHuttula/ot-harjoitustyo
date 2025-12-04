"""Register view module for user registration interface."""

from tkinter import ttk, StringVar
from ui.base_view import BaseView


class RegisterView(BaseView):
    """UI component for user registration."""

    def __init__(self, root, register_handler, login_handler):
        """Initialize register view.

        Args:
            root: Parent Tk widget
            register_handler: Callback for registration
            login_handler: Callback to navigate to login view
        """
        super().__init__(root)
        self._register_handler = register_handler
        self._login_handler = login_handler
        self._username_entry = None
        self._password_entry = None
        self._confirm_entry = None
        self._initialize()

    def _validate_inputs(self, username, password, confirm):
        """Validate registration form inputs.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not username or not password:
            return False, "Username and password is required"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if password.isalpha():
            return False, "Password must contain at least one number or special character"
        
        if not confirm:
            return False, "Please confirm your password"
        
        if password != confirm:
            return False, "Passwords do not match"
        
        return True, ""

    def _register_handler_wrapper(self):
        """Handle registration form submission."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        confirm = self._confirm_entry.get() if self._confirm_entry else None

        is_valid, error_msg = self._validate_inputs(username, password, confirm)
        if not is_valid:
            self._error(error_msg)
            return
        
        try:
            self._register_handler(username, password)
            self._login_handler()
        except Exception as e:
            self._error(str(e))

    def _login_handler_wrapper(self):
        """Navigate to login view."""
        self._login_handler()

    def _initialize(self):
        """Initialize the register view UI components."""
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
        self._confirm_entry = self._create_form_field(3, "Confirm password", show_char="*")

        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._register_handler_wrapper
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Go to Login",
            command=self._login_handler_wrapper
        )
        register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        login_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
