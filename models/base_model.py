#!/usr/bin/python3

"""This module is the base of the console of the project
Defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes all methods and instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """prints the instances"""
        return ("[{}] ({}) {}".format(
            self.__class__, self.id, self.__dict__
        ))
    
    def save(self):
        """updates the public instance attribute update_at
        with current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionay containing all keys/values
        of __dict__ of the instances"""
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()