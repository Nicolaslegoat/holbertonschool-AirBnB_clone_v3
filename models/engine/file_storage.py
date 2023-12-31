#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        self.reload()


    def get(self, cls, id):
        """A method to retrieve one object"""
        dictionnary_object = self.__objects.items()
        key_concat = cls.__name__ + "." + id

        for key, value in dictionnary_object:
            if key_concat == key:
                return value

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        dictionnary_object = self.__objects.items()
        count = 0

        if cls is None:
            return len(dictionnary_object)
        else:
            for key, value in dictionnary_object:
                if cls == type(value):
                    count += 1
        return count
