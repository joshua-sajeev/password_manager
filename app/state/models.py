import pynecone as pc
class accounts(pc.Model, table=True):
    email: str 
    username: str
    app_name: str
    password: str