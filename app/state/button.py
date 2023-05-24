import pynecone as pc
from .state import State
from .models import accounts
import mysql.connector as mc




class MyState(State):
    """State for different mysql operation"""
    password_feild: str=""
    old_password: str=""
    email_feild: str="" 
    username_feild: str=""
    app_name_feild: str=""

    def add_password(self):
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
            return pc.window_alert("Password Added")
        except(Exception):
            pass    
        
    def clear_text(self):
        self.email_feild=""
        self.password_feild=""
        self.username_feild=""
        self.app_name_feild=""
        self.old_password=""

    def update_password(self):
        with pc.session() as session:
            # Query the User record corresponding to the provided email
            user = (session.query(accounts
                          ).filter(
                            accounts.email==self.email_feild
                          ).filter(
                            accounts.password==self.old_password
                            ).update({
                               accounts.password: self.password_feild
                               })
            )
            # If a user is found with the given email and old_password
            if user:
                session.commit()
                return pc.window_alert("Password updated successfully")
            else:
                # No matching user found
                return pc.window_alert("Invalid email address or password. Please try again.")

    def delete_password(self):
        with pc.session() as session:
            # Query the User record corresponding to the provided email
            user = (session.query(accounts
                                  ).filter(accounts.email==self.email_feild
                                           ).filter(accounts.username==self.username_feild
                                                    ).filter(accounts.password==self.password_feild
                                                            ).delete()
            )
            # If a user is found with the given email and old_password
            if user:
                session.commit()
                return pc.window_alert("Password deleted successfully")
            else:
                # No matching user found
                return pc.window_alert("Invalid email address or password. Please try again.")
