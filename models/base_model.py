#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base class for all other classes in this project """

    def __init__(self, *args, **kwargs):
        """ Initialize public attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)

    def reload(self):
        """ Reload the current instance from the storage """
        models.storage.reload()

    def __repr__(self):
        """ Return a string representation of the BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)

    def reload(self):
        """ Reload the current instance from the storage """
        models.storage.reload()

    def __repr__(self):
        """ Return a string representation of the BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
