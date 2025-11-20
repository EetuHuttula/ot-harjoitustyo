"""Authentication service module."""
from repository.user_repository import add_user, verify_password


def register_handler(ui, username, password):
    """Handle user registration.

    Args:
        ui: The UI/controller instance
        username: The username to register
        password: The password for the user
    """
    add_user(username, password)
    if hasattr(ui, "show_message"):
        ui.show_message("Registered successfully")


def login_handler(ui, username=None, password=None, on_success=None):
    """Handle login logic. If username and password are provided,
     check credentials. If not, show login view."""
    if username is not None and password is not None:
        result = verify_password(username, password)
        if result and on_success:
            on_success(username)
        return result
    if hasattr(ui, "show_login_view"):
        ui.show_login_view()
    return None
