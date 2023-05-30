import pynecone as pc
from .state import State


class LoginState(State):
    """State for the login form."""

    password: str = ""

    def log_in(self):
            if self.password =="ADMIN_KEY":
                return pc.redirect("/menu")
            else:
                return pc.window_alert("Wrong password.")

