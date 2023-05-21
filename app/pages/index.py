import pynecone as pc
from .login import login

def index():
    login_container=pc.container(
            pc.vstack(
                pc.container(height="65px"),
                pc.container(
                    pc.text("Password Manager",
                            fontSize="28px",
                            color="white",
                            fontWeight="bold",
                            letterSpacing="2px"
                        ),
                    width="450px",
                    center_content=True,
                ),
                pc.container(
                    pc.text("""This is a simple Password Manager app,it is for a single user who can login using the
                            admin password. A user can add new passwords, edit, update, and see. Passwords are hashed before saving.""",
                            fontSize="20px",
                            color="white",
                            fontWeight="bold",
                            letterSpacing="2px"
                        ),
                    width="auto",
                    center_content=True,
                ),
                pc.container(height="8vh"),
                pc.container(
                    pc.container(height="5px"),
                    pc.container(
                        pc.link(
                            pc.button("Get Started",underline="none"),
                            href="/login",
                        ),
                        width="450px",
                        center_content=True,

                    ),
                ),
                               
            ),
            width="850px",
            height="75vh",
            g="#1D2330",
            borderRadius="15px",
            boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",
        )
    _main=pc.container(
            login_container,
            center_content=True,
            justifyContent="center",
            maxWidth="auto",
            height="100vh",
            bg="#1d2330",
            )
    return _main