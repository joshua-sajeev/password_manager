import pynecone as pc
from .models import User
from .state import State


class LoginState(State):
    """State for the login form."""

    password: str = "we"

    def log_in(self):
            if self.password =="ADMIN_KEY":
                return pc.redirect("/menu")
            else:
                return pc.window_alert("Wrong password.")

    def log_out(self):
        self.user = None
        return pc.redirect("/")
