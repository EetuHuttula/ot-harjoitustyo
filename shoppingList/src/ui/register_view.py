from tkinter import ttk, StringVar, constants

class RegisterView:
    def __init__(self, root, register_handler, login_handler):
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
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _error(self, message):
        self._message_variable.set(message)
    
    def _register_handler_wrapper(self):
        username = self._username_entry.get()

        password = self._password_entry.get()
        
        confirm = None
        if self._confirm_entry:
            confirm = self._confirm_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._error("Username and password is required")
            return
        
        if len(password) < 3:
            self._error("Password must be at least 3 characters long")
            return
        
        if username.isalpha():
            self._error("Password must contain at least one number or special character")
            return
        
        if confirm is None or len(confirm) == 0:
            self._error("Please confirm your password")
            return

        if password != confirm:
            self._error("Passwords do not match")
            return
        try:
            self._register_handler(username, password)
        except Exception as e:
            self._error(str(e))
        confirm = self._confirm_entry.get() if self._confirm_entry else None

    # AI GENEROITU KOODI ALKAA

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, padx=5, pady=5)
    
    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(row=2, column=0, padx=5, pady=5) 
        self._password_entry.grid(row=2, column=1, padx=5, pady=5)
    
    def _initialize_password_field_confirmation(self):
        confirm_label = ttk.Label(master=self._frame, text="Confirm password")
        self._confirm_entry = ttk.Entry(master=self._frame, show="*")
        confirm_label.grid(row=3, column=0, padx=5, pady=5)
        self._confirm_entry.grid(row=3, column=1, padx=5, pady=5)

    # AI GENEROITU KOODI LOPPUU

    def _initialize(self):
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
            command=self._login_handler
        )
        register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        login_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)