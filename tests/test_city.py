#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os
import json


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test instantiation of City class with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of City is stored in __objects attr."""
        self.assertIn(City(), City._FileStorage__objects.values())

    def test_id_is_public_str(self):
        """Test that id attribute is a public class attribute and is a str."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at attribute is public and is a datetime."""
        self.assertEqual(datetime, type(City().created_at))


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    def test_save_updates_updated_at(self):
        """Test that save method updates the updated_at attribute."""
        inst = City()
        old_updated_at = inst.updated_at
        sleep(0.1)
        inst.save()
        self.assertLess(old_updated_at, inst.updated_at)

    def test_save_updates_updated_at_filestorage(self):
        """Test that save method updates the updated_at attribute in storage."""
        inst = City()
        old_updated_at = inst.updated_at
        sleep(0.1)
        inst.save()
        key = inst.__class__.__name__ + '.' + inst.id
        self.assertLess(
            old_updated_at, City._FileStorage__objects[key].updated_at)

    def test_save_saves_to_file(self):
        """Test that save method saves updated object to file"""
        inst = City()
        key = inst.__class__.__name__ + '.' + inst.id
        os.remove("file.json")
        inst.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r") as f:
            self.assertIn(key, json.load(f))

    def test_save_saves_to_file_filestorage(self):
        """Test that save method saves updated object to filestorage"""
        inst = City()
        key = inst.__class__.__name__ + '.' + inst.id
        os.remove("file.json")
        inst.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r") as f:
            self.assertIn(key, json.load(f))

    def test_save_no_args(self):
        """Test that save method has no args"""
        with self.assertRaises(TypeError):
            City.save()


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test type of return from to_dict method."""
        inst = City()
        self.assertEqual(dict, type(inst.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test keys in to_dict dictionary."""
        inst = City()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test keys in to_dict dictionary."""
        inst = City()
        inst.new_attr = "value"
        inst.my_number = 89
        self.assertIn("new_attr", inst.to_dict())
        self.assertIn("my_number", inst.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test datetime values are strings."""
        inst = City()
        self.assertEqual(str, type(inst.to_dict()["created_at"]))
        self.assertEqual(str, type(inst.to_dict()["updated_at"]))

    def test_to_dict_output(self):
        """Test dictionary output from to_dict method."""
        inst = City()
        inst_dict = inst.to_dict()
        self.assertEqual(inst_dict["__class__"], "City")
        self.assertEqual(type(inst_dict["created_at"]), str)
        self.assertEqual(type(inst_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
