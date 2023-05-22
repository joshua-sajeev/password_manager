import pynecone as pc

class AppConfig(pc.Config):
    pass

config = pc.Config(
    app_name="app",
    db_url="mysql+mysqlconnector://root:joshua@localhost:3306/PasswordManager",
)