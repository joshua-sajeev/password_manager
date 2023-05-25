import pynecone as pc
from .menu import menu
from app.state.login import LoginState

def login():
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
                    pc.text("Type in your Admin Password",
                            fontSize="18px",
                            color="#f2fbfd",
                            fontWeight="bold",
                            letterSpacing="2px"
                        ),
                    width="450px",
                    center_content=True,
                ),
                pc.container(height="8vh"),
                pc.container(
                    pc.hstack(
                        pc.icon(
                            tag="lock",
                            color="white",
                            fontSize="22px",
                        ),
                        pc.password(
                            placeholder="Password",
                            border="0px",
                            focus_border_color="white",
                            color="white",
                            fontWeight="semibold",
                            fontSize="22px",
                            on_change=LoginState.set_password,
                            on_key_down=LoginState.on_key_down,
                        ),
                        width="550px",
                        center_content=True,
                    ),
                    pc.container(height="5px"),
                    pc.container(
                            pc.button("Sign In",on_click=LoginState.log_in),
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
