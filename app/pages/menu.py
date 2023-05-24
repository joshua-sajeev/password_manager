import pynecone as pc

def menu():
    login_container=pc.container(
            pc.vstack(
                pc.container(height="15vh"),
                pc.button("Create",width="100px",on_click=pc.redirect("/create")),
                pc.button("Update",size="md",on_click=pc.redirect("/update")),
                pc.button("Delete",size="md"),
                pc.button("Show All",size="md"),
                pc.button("Find Password",size="md"),
                pc.button("Find Accounts",size="md"),
            ),
            width="1050vh",
            height="75vh",
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
