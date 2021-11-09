0;136;0c0;136;0c#!/usr/bin/python3
"""This module contains the prototype for BaseModel class."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the AirBnB project."""
    
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
