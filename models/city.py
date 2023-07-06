#!/usr/bin/python3
"""module to store main class."""
from models.base_model import BaseModel

"""City models"""


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'state_id' not in kwargs:
            self.state_id = ""