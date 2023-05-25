import pynecone as pc
from app.pages.login import login
from app.pages.index import index
from app.pages.menu import menu
from app.pages.create import create
from app.pages.update import update
from app.pages.delete import delete
from app.pages.findpw import findpw
from app.state.state import State

app=pc.App(state=State)
app.add_page(index,title="Password Manager")
app.add_page(login,title="Password Manager")
app.add_page(menu,title="Password Manager")
app.add_page(update,title="Password Manager")
app.add_page(create,title="Password Manager")
app.add_page(delete,title="Password Manager")
app.add_page(findpw,title="Password Manager")

app.compile()
