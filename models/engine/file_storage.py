#!/usr/bin/python3
"""This module contains the prototype for FileStorage class."""
import json


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)
