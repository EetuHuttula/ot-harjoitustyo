"""Register view module for user registration interface."""

from tkinter import ttk, StringVar, constants


class RegisterView:
    """UI component for user registration."""

    def __init__(self, root, register_handler, login_handler):
        """Initialize register view.

        Args:
            root: Parent Tk widget
            register_handler: Callback for registration
            login_handler: Callback to navigate to login view
        """
        self._root = root
        self._register_handler = register_handler
        self._login_handler = login_handler
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._confirm_entry = None
        self._message_variable = None
        self._initialize()

    def pack(self):
        """Pack the frame into the parent widget."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the frame and its contents."""
        self._frame.destroy()

    def _error(self, message):
        """Display error message.

        Args:
            message: Error message to display
        """
        self._message_variable.set(message)

    def _register_handler_wrapper(self):
        """Handle registration form submission."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        confirm = None
        if self._confirm_entry:
            confirm = self._confirm_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._error("Username and password is required")
            return

        if len(username) < 3:
            self._error("Password must be at least 3 characters long")
            return
        if len(password) < 8:
            self._error("Password must be at least 8 characters long")
            return
        if password.isalpha():
            self._error(
                "Password must contain at least one number or special character")
            return

        if confirm is None or len(confirm) == 0:
            self._error("Please confirm your password")
            return

        if password != confirm:
            self._error("Passwords do not match")
            return
        try:
            self._register_handler(username, password)
            # On success, navigate to login view
            self._login_handler()
        except Exception as e:
            self._error(str(e))

    # AI generated starts
    def _initialize_username_field(self):
        """Initialize username input field."""
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, padx=5, pady=5)

    def _initialize_password_field(self):
        """Initialize password input field."""
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, padx=5, pady=5)

    def _initialize_password_field_confirmation(self):
        """Initialize password confirmation input field."""
        confirm_label = ttk.Label(master=self._frame, text="Confirm password")
        self._confirm_entry = ttk.Entry(master=self._frame, show="*")
        confirm_label.grid(row=3, column=0, padx=5, pady=5)
        self._confirm_entry.grid(row=3, column=1, padx=5, pady=5)
    # Ai generated ends

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

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_password_field_confirmation()

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

    def _login_handler_wrapper(self):
        """Navigate to login view."""
        self._login_handler()
