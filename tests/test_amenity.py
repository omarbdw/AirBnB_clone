#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Sets up test methods"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down test methods"""
        del self.amenity

    def test_name(self):
        """Tests that name is an empty string"""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Tests that Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
