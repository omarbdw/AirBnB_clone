#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Sets up test methods"""
        self.review = Review()

    def tearDown(self):
        """Tears down test methods"""
        del self.review

    def test_inheritance(self):
        """Tests that Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Tests that Review has the expected attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
