#!/usr/bin/python3
"""module to store main class."""
import uuid
from models.base_model import BaseModel

"""User models"""


class User(BaseModel):
    """user class."""
    str = ""
    password = ""
    first_name = ""
    last_name = ""
