#!/usr/bin/python3
import uuid
from datetime import datetime
"""Base models"""


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        from models.engine.file_storage import FileStorage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if type(value) is str:
                        """checks for all parsed datetime variables"""
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage().new(self)

    def __str__(self):
        """return the string representation"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Update the date variable"""
        import models
        self.updated_at = datetime.now()
        models.storage.save()

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
