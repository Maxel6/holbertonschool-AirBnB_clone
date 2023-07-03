#!/usr/bin/python3
"""Import uuid and datetime modules"""
import uuid
import datetime
"""Base models"""


class BaseModel:
    """base class"""

    def __init__(self):
        """Initialize instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the date variable"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """update and return __dict__"""
        iso_updated = self.updated_at.isoformat()
        iso_created = self.created_at.isoformat()
        self.__dict__["__class__"].append(self.__class__.__name__)
        return self.__dict__
