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
        with open(self.__file_path, 'w', encoding='utf-8') as output_file:
            json.dump(self.__objects, output_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, 'r') as input_file:
                self.__objects = json.load(input_file)
        else:
            pass
