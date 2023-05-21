import pynecone as pc

class AppConfig(pc.Config):
    pass

config = AppConfig(
    app_name="app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)