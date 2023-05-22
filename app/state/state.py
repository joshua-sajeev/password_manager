from typing import Optional
import pynecone as pc
from .models import User,accounts


class State(pc.State):
    """The app state."""

    user: Optional[User] = None
