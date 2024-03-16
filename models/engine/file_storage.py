#!/usr/bin/python3
"""Module for FileStorage class"""

import json
import uuid
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # Check if the object has an 'id' attribute
        if hasattr(obj, 'id'):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
        else:
            # Handle objects without an 'id' attribute here
            obj.id = str(uuid.uuid4())
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    if cls_name == "User":
                        cls = User
                    elif cls_name == "State":
                        cls = State
                    elif cls_name == "City":
                        cls = City
                    elif cls_name == "Amenity":
                        cls = Amenity
                    elif cls_name == "Place":
                        cls = Place
                    elif cls_name == "Review":
                        cls = Review
                    else:
                        cls = BaseModel
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def find_by_id(self, cls, id):
        """Find object by class name and id"""
        key = "{}.{}".format(cls.__name__, id)
        return self.__objects.get(key)
