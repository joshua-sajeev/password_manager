import pynecone as pc
from app.state.button import MyState

def create():
    custom_icon = pc.image(
    src="/home/joshua/Python/app/assets/bg.svg",
    alt="Custom icon",
    width=24,
    height=24
    )
    container=pc.container(
            pc.vstack(
                pc.box(height="2vh"),
                pc.container(
                    pc.hstack(
                        pc.link(pc.icon(tag="chevron_left")
                                ,underline="none",
                                fontSize="35px",
                                href="/menu"
                                ),
                        pc.spacer(flex=1),
                        pc.heading("Type in your Details"),
                        color="#f2fbfd",
                        fontWeight="semibold",
                        width="500px",
                        center_content=True,
                    ),
                ),
                pc.box(height="2vh"),
                pc.hstack(
                    pc.icon(
                            tag="email",
                            color="white",
                            fontSize="22px",
                        ),
                        pc.input(
                            placeholder="email",
                            color="white",
                            value=MyState.email_feild,
                            on_change=MyState.set_email_feild,
                        )
                ), 
                pc.box(height="2vh"),
                pc.hstack(
                    pc.icon(
                            tag="lock",
                            color="white",
                            fontSize="22px",
                        ),
                        pc.input(
                            placeholder="password",
                            color="white",
                            value=MyState.password_feild,
                            on_change=MyState.set_password_feild,
                        )
                ),
                pc.box(height="2vh"),
                pc.hstack(
                    pc.icon(
                            tag="at_sign",
                            color="white",
                            fontSize="22px",
                        ),
                        pc.input(
                            placeholder="username",
                            color="white",
                            value=MyState.username_feild,
                            on_change=MyState.set_username_feild,
                        )
                ), 
                pc.box(height="2vh"),  
                pc.hstack(
                    pc.icon(
                            tag="drag_handle",
                            color="white",
                            fontSize="22px",
                        ),
                        pc.input(
                            placeholder="app name",
                            color="white",
                            value=MyState.app_name_feild,
                            on_change=MyState.set_app_name_feild,
                        )
                ),
                pc.box(height="2vh"),
                pc.hstack(
                    pc.button("Add",on_click=MyState.add_password),
                    pc.button("Clear",on_click=MyState.clear_text)                      
                )
            ),
            width="850px",
            height="70vh",
            g="#1D2330",
            borderRadius="15px",
            boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",
        )
    _main=pc.container(
            container,
            center_content=True,
            justifyContent="center",
            maxWidth="auto",
            height="100vh",
            bg="#1d2330",
            )
    return _main
