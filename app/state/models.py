import pynecone as pc


class User(pc.Model, table=True):
    email: str
    password: str


class accounts(pc.Model, table=True):
    password: str
    email: str 
    username: str
    app_name: str