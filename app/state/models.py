import pynecone as pc


class User(pc.Model, table=True):
    password: str


class accounts(pc.Model, table=True):
    email: str 
    username: str
    app_name: str
    password: str