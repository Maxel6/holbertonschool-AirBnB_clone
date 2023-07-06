#!/usr/bin/python3
"""module to store main class."""
from models.base_model import BaseModel

"""Review models"""


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'place_id' not in kwargs:
            self.place_id = ""
        if 'user_id' not in kwargs:
            self.user_id = ""
        if 'text' not in kwargs:
            self.text = ""
