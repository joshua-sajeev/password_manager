import pynecone as pc

config = pc.Config(
    app_name="app",
    db_url="mysql+mysqlconnector://root:joshua@localhost:3306/PasswordManager",
)