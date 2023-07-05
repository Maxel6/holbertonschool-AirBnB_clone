#!/usr/bin/python3
"""class to serialize and deserialize"""
import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
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
        from models import base_model
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as input_file:
                try:
                    jsoned_obj = json.load(input_file)
                except json.JSONDecodeError:
                    pass
                for key, value in jsoned_obj.items():
                    class_name = value['__class__']
                    class_obj = getattr(base_model, class_name)

                    obj = class_obj(**value)
                    self.__objects[key] = obj
                    self.new(obj)
        else:
            pass
