#!/usr/bin/python3
"""Base Model Module"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        try:
                            setattr(
                                    self,
                                    key,
                                    datetime.strptime(
                                        value,
                                        "%Y-%m-%dT%H:%M:%S.%f")
                                    )
                        except ValueError:
                            setattr(self, key, None)
                    else:
                        setattr(self, key, value)
        else:
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
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the BaseModel instance"""
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
