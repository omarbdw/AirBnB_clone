#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Sets up test methods"""
        self.user = User()

    def tearDown(self):
        """Tears down test methods"""
        del self.user

    def test_email(self):
        """Tests the email attribute"""
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """Tests the password attribute"""
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """Tests the first_name attribute"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """Tests the last_name attribute"""
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
