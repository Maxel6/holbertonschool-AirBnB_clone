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
        jsoned_obj = {}
        for key, obj in self.__objects.items():
            jsoned_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as output_file:
            json.dump(jsoned_obj, output_file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as input_file:
                jsoned_obj = json.load(input_file)
                for key, value in jsoned_obj.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_obj["__class__"])(**class_obj)
                    instance = class_obj(**value)
                    self.__objects[key] = instance
        else:
            pass
