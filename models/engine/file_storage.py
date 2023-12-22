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
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
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
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it's inside"""
        try:
            # Check if obj is provided
            if obj is not None:
                # Generate a unique key for obj
                key = obj.to_dict()['__class__'] + '.' + obj.id

                # Attempt to delete obj from __objects using the key
                del FileStorage.__objects[key]
        except KeyError:
            # Ignore if the key doesn't exist in __objects
            pass

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """A method to retrieve one object"""
        dictionnary_object = self.__objects.items()
        key_concat = cls.__name__ + "." + id

        for key, value in dictionnary_object:
            if key_concat == key:
                return value
        return "Get success"

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        if cls is None:
            return len(self.__objects)
        else:
            count = 0
            for key, value in self.__objects.items():
                if cls == type(value):
                    count += 1
            return count
