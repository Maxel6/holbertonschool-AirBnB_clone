#!/usr/bin/python3
import uuid
import datetime
"""Base models"""


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        if kwargs is True:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
            if key != '__class__':
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Update the date variable"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """turns instance into dict

        Returns:
            dict: dict form of instance
        """
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = type(self).__name__
        if not isinstance(copy_dict['created_at'], str):
            copy_dict['created_at'] = self.created_at.isoformat()
        if not isinstance(copy_dict['updated_at'], str):
            copy_dict['updated_at'] = self.updated_at.isoformat()
        return (copy_dict)
