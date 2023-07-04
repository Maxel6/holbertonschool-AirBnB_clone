#!/usr/bin/python3
import uuid
import datetime
"""Base models"""


class BaseModel:
    """base class"""

    def __init__(self, **kwargs):
        """Initialize instance"""
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.datetime.now()
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """return the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Update the date variable"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """update and return __dict__"""
        if isinstance(self.created_at, datetime.datetime):
            self.__dict__['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime.datetime):
            self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__

        return self.__dict__
