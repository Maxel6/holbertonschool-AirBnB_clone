#!/usr/bin/python3
import uuid
import datetime
"""Base models"""

class BaseModel:
    """base class"""

    def __init__(self):
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
        self.updated_at = self.updated_at.isoformat()

        self.created_at = self.created_at.isoformat()
     
        self.__dict__["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            print(f"{key}: ({type(value)}) - {value}")
        return self.__dict__
