#!/usr/bin/python3
"""class to serialize and deserialize"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        with open(self.__file_path, 'r') as file:
            if file:
                self.__objects = json.load(file)
            else:
                pass
