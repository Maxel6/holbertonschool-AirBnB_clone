#!/usr/bin/python3
"""module to store main class."""
from models.base_model import BaseModel

"""Place models"""


class Place(BaseModel):
    """Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'city_id' not in kwargs:
            self.city_id = ""
        if 'user_id' not in kwargs:
            self.user_id = ""
        if 'name' not in kwargs:
            self.name = ""
        if 'description' not in kwargs:
            self.description = ""
        if 'number_rooms' not in kwargs:
            self.number_rooms = 0
        if 'number_bathrooms' not in kwargs:
            self.number_bathrooms = 0
        if 'max_guest' not in kwargs:
            self.max_guest = 0
        if 'price_by_night' not in kwargs:
            self.price_by_night = 0
        if 'latitude' not in kwargs:
            self.latitude = 0.0
        if 'longitude' not in kwargs:
            self.longitude = 0.0
        if 'amenity_ids' not in kwargs:
            self.amenity_ids = []
