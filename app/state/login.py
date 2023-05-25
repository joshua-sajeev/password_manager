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

    def on_key_down(self, key):
        if key == "Enter":
            if self.password =="ADMIN_KEY":
                return pc.redirect("/menu")
            else:
                return pc.window_alert("Wrong password.")

            

