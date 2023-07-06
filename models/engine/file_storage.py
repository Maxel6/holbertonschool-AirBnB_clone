#!/usr/bin/python3
"""class to serialize and deserialize"""
import json
import os
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City


class FileStorage:
    """Class used to store datas

    Returns:
        class: multiples methods to deal with instances and stock them in json
        files
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns objects of instance

        Returns:
            dict: dict to be inspected
        """
        return self.__objects

    def new(self, obj):
        """creates new instance in dict

        Args:
            obj (dict): new dict form from instance
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        obj_list = {}
        for k, v in self.__objects.items():
            obj_list[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            json.dump(obj_list, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    if class_name in classes:
                        cls = classes[class_name]
                        obj = cls(**value)
                        self.__objects[key] = obj
