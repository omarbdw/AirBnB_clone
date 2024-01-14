#!/usr/bin/python3
""""""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Sets up test methods"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_file_path(self):
        """Tests that file_path is a string"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        """Tests that objects is a dictionary"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Tests that all returns the __objects attribute"""
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new(self):
        """Tests that new adds an object to __objects"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + '.' + model.id
        self.assertIn(key, self.storage.all())

    def test_reload(self):
        """Tests that reload deserializes the JSON file to __objects"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = model.__class__.__name__ + '.' + model.id
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
