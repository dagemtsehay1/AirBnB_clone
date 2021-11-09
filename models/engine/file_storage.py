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
