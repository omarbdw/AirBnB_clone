#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Sets up test methods"""
        self.city = City()

    def tearDown(self):
        """Tears down test methods"""
        del self.city

    def test_inheritance(self):
        """Tests that City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Tests that City has the correct attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
