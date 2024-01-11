#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from datetime import datetime
from uuid import UUID
import json
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Sets up test methods"""
        self.model = BaseModel()

    def tearDown(self):
        """Tears down test methods"""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_uuid(self):
        """Tests that the id is a valid uuid"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(UUID(self.model.id), UUID)

    def test_created_at(self):
        """Tests that created_at is a valid datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Tests that updated_at is a valid datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Tests that save updates the updated_at attribute"""
        old_time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_time, self.model.updated_at)

    def test_to_dict(self):
        """Tests that to_dict returns the correct dictionary"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertIsInstance(model_dict["__class__"], str)

    def test_str(self):
        """Tests that the str method has the correct output"""
        string = "[{}] ({}) {}".format(
            self.model.__class__.__name__,
            self.model.id,
            self.model.__dict__
        )
        self.assertEqual(string, str(self.model))

    def test_kwargs(self):
        """Tests that kwargs are correctly handled"""
        model_dict = self.model.to_dict()
        model_copy = BaseModel(**model_dict)
        self.assertEqual(self.model.id, model_copy.id)
        self.assertEqual(self.model.created_at, model_copy.created_at)
        self.assertEqual(self.model.updated_at, model_copy.updated_at)
        self.assertEqual(self.model.__class__.__name__,
                         model_copy.__class__.__name__)
        self.assertEqual(self.model.__dict__, model_copy.__dict__)

    def test_save_file(self):
        """Tests that save writes to a file"""
        self.model.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_contents(self):
        """Tests that save writes the correct contents to a file"""
        self.model.save()
        with open("file.json", "r") as f:
            self.assertIn(self.model.id, f.read())

    def test_save_file_contents_reload(self):
        """Tests that save writes the correct contents to a file"""
        self.model.save()
        model_copy = BaseModel(**self.model.to_dict())
        with open("file.json", "r") as f:
            self.assertIn(model_copy.id, f.read())


if __name__ == '__main__':
    unittest.main()
