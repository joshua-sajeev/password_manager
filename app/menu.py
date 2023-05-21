import pynecone as pc

def get_input_field(icon: str, placeholder: str, _type: str):
    return pc.container(
        pc.hstack(
            pc.icon(
                tag=icon,
                color="white",
                fontSize="22px",
            ),
            pc.input(
                placeholder=placeholder,
                border="0px",
                focus_border_color="white",
                color="white",
                fontWeight="semibold",
                fontSize="22px",
                type=_type,
            )
        )
    )

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
                        ),
                        width="auto",
                        center_content=True,
                    ),
                    pc.container(height="5px"),
                    pc.container(
                        pc.link(
                            pc.button("Sign In",underline="none"),
                            href="/menu.py",
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
