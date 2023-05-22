import pynecone as pc
from .state import State
from .models import accounts
import mysql.connector as mc




class MyState(State):
    """State for different mysql operation"""
    password_feild: str=""
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
        self.app_name_feild="   "

