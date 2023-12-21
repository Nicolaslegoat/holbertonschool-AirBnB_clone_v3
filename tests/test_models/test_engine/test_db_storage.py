#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.user import User
import os
from MySQLdb import _mysql


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """
    def test_all(self):
        """ test all() function """
        new = City()
        storage.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_methods(self):
        """ test presence of methods """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'delete'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_get_count():
        """Test .get() and .count() methods"""
        from models import storage
        from models.state import State

        print("All objects: {}".format(storage.count()))
        print("State objects: {}".format(storage.count(State)))

        first_state_id = list(storage.all(State).values())[0].id
        print("First state: {}".format(storage.get(State, first_state_id)))


if __name__ == "__main__":
    unittest.main()
