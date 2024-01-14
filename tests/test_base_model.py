#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from datetime import datetime
from uuid import UUID
import json
import os
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """Tests that to_dict returns a dictionary"""
        inst = BaseModel()
        self.assertEqual(dict, type(inst.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Tests dict contains all keys required by BaseModel"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        inst = BaseModel()
        inst_dict = inst.to_dict()
        for k in keys:
            self.assertIn(k, inst_dict)

    def test_to_dict_contains_added_attributes(self):
        """Tests dict contains added attributes"""
        inst = BaseModel()
        inst.name = "Holberton"
        inst.my_number = 98
        inst_dict = inst.to_dict()
        self.assertIn("name", inst_dict)
        self.assertIn("my_number", inst_dict)

    def test_to_dict_datetime(self):
        """Tests to_dict converts datetime to isoformat"""
        inst = BaseModel()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst_dict = inst.to_dict()
        self.assertEqual(inst.created_at.isoformat(),
                         inst_dict["created_at"])
        self.assertEqual(inst.updated_at.isoformat(),
                         inst_dict["updated_at"])
        self.assertEqual(time_format, "%Y-%m-%dT%H:%M:%S.%f")

    def test_to_dict_classname(self):
        """Tests to_dict adds the class name as __class__"""
        inst = BaseModel()
        inst_dict = inst.to_dict()
        self.assertEqual("BaseModel", inst_dict["__class__"])

    def test_to_dict_output(self):
        """Tests to_dict has the correct output"""
        inst = BaseModel()
        inst.id = "123"
        inst.name = "Holberton"
        inst.my_number = 98
        inst_dict = inst.to_dict()
        model = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(inst_dict["id"], "123")
        self.assertEqual(inst_dict["name"], "Holberton")
        self.assertEqual(inst_dict["my_number"], 98)
        self.assertEqual(inst_dict["__class__"], "BaseModel")
        self.assertEqual(inst_dict["created_at"],
                         inst.created_at.isoformat())
        self.assertEqual(inst_dict["updated_at"],
                         inst.updated_at.isoformat())
        self.assertEqual(str, type(inst_dict["created_at"]))
        self.assertEqual(str, type(inst_dict["updated_at"]))
        self.assertEqual(model, inst_dict["__class__"])


class TestBaseModel_init(unittest.TestCase):
    """Unittests for testing the init method of the BaseModel class."""

    def test_init_no_args(self):
        """Tests init with no arguments"""
        inst = BaseModel()
        self.assertEqual(BaseModel, type(inst))

    def test_init_kwargs(self):
        """Tests init with kwargs given"""
        inst = BaseModel(id="123", name="Holberton", my_number=98)
        self.assertEqual(BaseModel, type(inst))
        self.assertEqual("Holberton", inst.name)
        self.assertEqual(98, inst.my_number)
        self.assertEqual("123", inst.id)

    def test_init_id(self):
        """Tests that id is a string"""
        inst = BaseModel()
        self.assertEqual(str, type(inst.id))

    def test_init_created_at(self):
        """Tests that created_at is datetime"""
        inst = BaseModel()
        self.assertEqual(datetime, type(inst.created_at))

    def test_init_updated_at(self):
        """Tests that updated_at is datetime"""
        inst = BaseModel()
        self.assertEqual(datetime, type(inst.updated_at))


class TestBaseModel_Save(unittest.TestCase):
    """Unittests for testing the save method of the BaseModel class."""

    def test_save(self):
        """Tests save updates updated_at"""
        inst = BaseModel()
        sleep(0.1)
        first_updated = inst.updated_at
        inst.save()
        second_updated = inst.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_save_updated_at_type(self):
        """Tests that updated_at is datetime"""
        inst = BaseModel()
        inst.save()
        self.assertEqual(datetime, type(inst.updated_at))

    def test_save_updated_at(self):
        """Tests save updates updated_at"""
        inst = BaseModel()
        sleep(0.1)
        first_updated = inst.updated_at
        inst.save()
        second_updated = inst.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_save_updated_at_value(self):
        """Tests save updates updated_at"""
        inst = BaseModel()
        sleep(0.1)
        first_updated = inst.updated_at
        inst.save()
        second_updated = inst.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_save_created_at_type(self):
        """Tests that created_at is datetime"""
        inst = BaseModel()
        inst.save()
        self.assertEqual(datetime, type(inst.created_at))

    def test_save_created_at(self):
        """Tests save updates created_at"""
        inst = BaseModel()
        sleep(0.1)
        first_created = inst.created_at
        inst.save()
        second_created = inst.created_at
        self.assertEqual(first_created, second_created)

    def test_save_created_at_value(self):
        """Tests save updates created_at"""
        inst = BaseModel()
        sleep(0.1)
        first_created = inst.created_at
        inst.save()
        second_created = inst.created_at
        self.assertEqual(first_created, second_created)


if __name__ == '__main__':
    unittest.main()
