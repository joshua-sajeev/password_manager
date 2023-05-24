import pynecone as pc
from app.pages.login import login
from app.pages.index import index
from app.pages.menu import menu
from app.pages.create import create
from app.pages.update import update
from app.pages.delete import delete
from app.state.state import State

app=pc.App(state=State)
app.add_page(index)
app.add_page(login)
app.add_page(menu)
app.add_page(create)
app.add_page(update)
app.add_page(delete)

app.compile()
