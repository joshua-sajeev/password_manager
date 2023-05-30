import pynecone as pc
from app.state.button import MyState
def menu():
    login_container=pc.container(
            pc.container(height="1vh"),
            pc.hstack(
                pc.spacer(),
                pc.link(
                    pc.icon(tag="close",on_mouse_down=MyState.clear_text()),
                    href="/login",
                    color="white",
                    _hover={
                                "color": "rgb(107,99,246)",
                            },
                    button=True,
                ),
            ),
            pc.vstack(
                pc.container(height="3vh"),
                pc.button("Create",width="100px",on_click=pc.redirect("/create"),),
                pc.container(height="1.5vh"),
                pc.button("Update",size="md",on_click=pc.redirect("/update")),
                pc.container(height="1.5vh"),
                pc.button("Delete",size="md",on_click=pc.redirect("/delete")),
                pc.container(height="1.5Vh"),
                pc.button("Find Password",size="md",on_click=pc.redirect("/findpw")),
            ),
            width="1050vh",
            height="55vh",
            bg="#1D2330",
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
