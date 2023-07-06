#!/usr/bin/python3
"""class to serialize and deserialize"""
import json
import os


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
        """
            Serialize __objects to the JSON file.
        """
        obj_list = {}
        for k, v in self.__objects.items():
            obj_list[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as out_file:
            json.dump(obj_list, out_file)

    def reload(self):
        """serializes and deserializes instances from json form"""
        from models.user import User
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as input_file:
                jsoned_obj = {}
                try:
                    jsoned_obj = json.load(input_file)
                except json.JSONDecodeError:
                    pass
                for key, value in jsoned_obj.items():
                    class_name = value['__class__']
                    if class_name == 'User':
                        class_obj = User
                    else:
                        class_obj = BaseModel

                    obj = class_obj(**value)
                    self.__objects[key] = obj
                    self.new(obj)
