import pynecone as pc


class User(pc.Model, table=True):
    password: str


class Contact(pc.Model, table=True):
    user_email: str
    contact_name: str
    email: str
    stage: str = "lead"
