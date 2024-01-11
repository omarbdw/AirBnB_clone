#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Sets up test methods"""
        self.state = State()

    def tearDown(self):
        """Tears down test methods"""
        del self.state

    def test_inheritance(self):
        """Tests that State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Tests that State has the correct attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_str(self):
        """Tests that the str method has the correct output"""
        string = "[{}] ({}) {}".format(
            self.state.__class__.__name__,
            self.state.id,
            self.state.__dict__
        )
        self.assertEqual(string, str(self.state))

    def test_to_dict(self):
        """Tests that to_dict returns the correct dictionary"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertIsInstance(state_dict["__class__"], str)
        self.assertEqual(state_dict["name"], self.state.name)


if __name__ == '__main__':
    unittest.main()
