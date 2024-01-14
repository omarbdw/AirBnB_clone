#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, mode="r"
                      , encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                if value["__class__"] == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
                elif value["__class__"] == "User":
                    FileStorage.__objects[key] = User(**value)
                elif value["__class__"] == "State":
                    FileStorage.__objects[key] = State(**value)
                elif value["__class__"] == "City":
                    FileStorage.__objects[key] = City(**value)
                elif value["__class__"] == "Amenity":
                    FileStorage.__objects[key] = Amenity(**value)
                elif value["__class__"] == "Place":
                    FileStorage.__objects[key] = Place(**value)
                elif value["__class__"] == "Review":
                    FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
