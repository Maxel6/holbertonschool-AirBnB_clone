#!/usr/bin/python3
import uuid
import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        iso_updated = self.updated_at.isoformat()
        iso_created = self.created_at.isoformat()
        self.__dict__["__class__"].append(self.__class__.__name__)
        return self.__dict__

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
