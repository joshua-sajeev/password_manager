import pynecone as pc
from app.state.button import MyState
def delete():
    container=pc.container(
            pc.vstack(
                pc.box(height="2vh"),
                pc.container(
                    pc.hstack(
                        pc.link(pc.icon(tag="chevron_left",on_mouse_down=MyState.clear_text()),
                                underline="none",
                                fontSize="35px",
                                href="/menu",
                                _hover={
                                    "color": "rgb(107,99,246)",
                                },
                                # on_click=MyState.clear_text,
                                ),
                        pc.spacer(flex=1),
                        pc.heading("Type in your Details"),
                        pc.spacer(flex=1),
                        pc.link(pc.icon(tag="close",on_mouse_down=MyState.clear_text()),
                                color="white",
                                href="/login",
                                _hover={
                                    "color": "rgb(107,99,246)",
                                },
                                # on_click=MyState.clear_text,
                            ),
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
                    pc.button("Delete",on_click=MyState.delete_password),
                    pc.button("Clear",on_click=MyState.clear_text)                      
                ),
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
