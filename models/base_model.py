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
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
