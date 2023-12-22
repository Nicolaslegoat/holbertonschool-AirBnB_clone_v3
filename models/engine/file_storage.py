#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    self.new(eval(cls_name)(**val))
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
