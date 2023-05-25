import pynecone as pc
from .state import State
from .models import accounts
from hash import make_password
import pyperclip as ppc
class MyState(State):
    """State for different mysql operation"""
    password_feild: str=""
    old_password: str=""
    new_password: str=""
    email_feild: str="" 
    username_feild: str=""
    app_name_feild: str=""

    def add_password(self):
        self.password_feild=make_password(self.old_password)
        try:
            with pc.session() as session:
                    session.add(
                        accounts(
                            username=self.username_feild, 
                            email=self.email_feild,
                            password=self.password_feild,
                            app_name=self.app_name_feild,
                        )
                    )
                    session.commit()
            self.find_password()
            return pc.window_alert("Password Added and Copied")
        except(Exception):
            pass    
        
    def clear_text(self):
        self.email_feild=""
        self.password_feild=""
        self.username_feild=""
        self.app_name_feild=""
        self.old_password=""

    def update_password(self):
        self.password_feild=make_password(self.new_password)
        with pc.session() as session:
            user = (session.query(accounts
                          ).filter(
                            accounts.email==self.email_feild
                          ).filter(
                            accounts.password==self.old_password
                            ).update({
                               accounts.password: self.password_feild
                               })
            )
            if user:
                session.commit()
                ppc.copy(user.password)
                return pc.window_alert("Password updated successfully")
            else:
                return pc.window_alert("Invalid email address or password. Please try again.")

    def delete_password(self):
        with pc.session() as session:
            user = (session.query(accounts
                                  ).filter(accounts.email==self.email_feild
                                           ).filter(accounts.username==self.username_feild
                                                    ).filter(accounts.password==self.password_feild
                                                            ).delete()
            )
            if user:
                session.commit()
                return pc.window_alert("Password deleted successfully")
            else:
                return pc.window_alert("Invalid email address or password. Please try again.")


    def find_password(self):
        with pc.session() as session:
            user = session.query(accounts).filter((accounts.username == self.username_feild) & (accounts.email == self.email_feild)).first()
            if user:
                ppc.copy(user.password)
                return pc.window_alert(f"Password copied to clipboard")
            else:
                return pc.window_alert("Can't find the password.Check your details again")
    