from repository.user_repository import add_user

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

def _login_handler(self, username=None, password=None, on_success=None):
    """Handle login logic. If username and password are provided, check credentials. If not, show login view."""
    from repository.user_repository import verify_password
    if username is not None and password is not None:
        result = verify_password(username, password)
        if result and on_success:
            on_success(username)
        return result
    if self.current_view:
        try:
            self.current_view.destroy()
        except Exception:
            pass
    from ui.login_view import LoginView
    self.current_view = LoginView(
        self._root,
        self._register_view,
        lambda u, p: self._login_handler(u, p, self._main_view)
    )
    self.current_view.pack()