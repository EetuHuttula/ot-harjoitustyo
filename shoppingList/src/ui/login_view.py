"""Register view module for user registration interface."""

from tkinter import ttk, StringVar, constants


class LoginView:
    """UI component for user registration."""

    def __init__(self, root, register_handler, login_handler):
        """Initialize register view.

        Args:
            root: Parent Tk widget
            register_handler: Callback to navigate to registration view
            login_handler: Callback for login logic
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

    def _login_handler_wrapper(self):
        """Handle login form submission."""
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._error("Username and password are required")
            return

        try:
            result = self._login_handler(username, password)
            if not result:
                self._error("Invalid username or password")
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

    def _register_handler_wrapper(self):
        """Navigate to registration view."""
        self._register_handler()
