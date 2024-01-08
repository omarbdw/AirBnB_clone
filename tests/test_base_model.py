import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_class_name(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['created_at'], self.model.created_at.isoformat())

    def test_to_dict_contains_updated_at(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()