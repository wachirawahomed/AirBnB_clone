#!/usr/bin/python3
"""Base Model Module"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
