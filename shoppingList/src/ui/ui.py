from ui.register_view import RegisterView
from repository.user_repository import add_user


class UI:
    def __init__(self, root):
        self._root = root
        self.current_view = None

    def start(self):
        self._register_view()

    def _register_view(self):
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass

        self.current_view = RegisterView(self._root, self._register_handler, self._login_handler)
        self.current_view.pack()

    def _register_handler(self, username, password):
        add_user(username, password)
        try:
            self.current_view._message_variable.set("Registered successfully")
        except Exception:
            pass
    def _login_handler(self):
        if self.current_view:
            try:
                self.current_view.destroy()
            except Exception:
                pass