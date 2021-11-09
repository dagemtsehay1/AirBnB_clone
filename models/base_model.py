#!/usr/bin/python3
"""This module contains the prototype for BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the AirBnB project."""
    
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    self.__dict__[k] = v
            
    def __str__(self):
        """Prints  [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
