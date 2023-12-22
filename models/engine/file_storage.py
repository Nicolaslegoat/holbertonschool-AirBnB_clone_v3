#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # If cls is specified, filter objects by the exact class type
        if cls is not None:
            filtered_objects = {}

            # Iterate through __objects to find the specified class type
            for key, obj in FileStorage.__objects.items():
                if type(obj) is cls:
                    # Add the object to the filtered list
                    filtered_objects[key] = obj

            # Return the filtered list of objects
            return filtered_objects
        else:
            # If cls is not specified, return all objects in __objects
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    self.new(classes[cls_name](**val))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """A method to retrieve one object"""
        key = "{}.{}".format(cls.__name__, id)
        return FileStorage.__objects.get(key, None)

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        if cls is None:
            return len(FileStorage.__objects)
        else:
            return sum(1 for obj in FileStorage.__objects.values()
                       if isinstance(obj, cls))
