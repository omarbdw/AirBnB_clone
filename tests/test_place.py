#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Sets up test methods"""
        self.place = Place()

    def tearDown(self):
        """Tears down test methods"""
        del self.place

    def test_inheritance(self):
        """Tests that Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Tests that Place has the correct attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, "")
        self.assertEqual(self.place.longitude, "")
        self.assertEqual(self.place.amenity_ids, [])

    def test_str(self):
        """Tests that the str method has the correct output"""
        string = "[{}] ({}) {}".format(
            self.place.__class__.__name__,
            self.place.id,
            self.place.__dict__
        )
        self.assertEqual(string, str(self.place))


if __name__ == '__main__':
    unittest.main()
