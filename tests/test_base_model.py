import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up"""
        self.model = BaseModel()

    def test_id(self):
        """Test id"""
        self.assertEqual(type(self.model.id), str)

    def test_created_at(self):
        """Test created_at"""
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at(self):
        """Test updated_at"""
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_str(self):
        """Test __str__"""
        self.assertEqual(str(self.model),
                         "[BaseModel] ({}) {}".format(self.model.id,
                                                      self.model.__dict__))

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual(type(self.model.to_dict()), dict)

    def test_save(self):
        """Test save"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_kwargs(self):
        """Test kwargs"""
        model_dict = self.model.to_dict()
        model2 = BaseModel(**model_dict)
        self.assertEqual(self.model.id, model2.id)
        self.assertEqual(self.model.created_at, model2.created_at)
        self.assertEqual(self.model.updated_at, model2.updated_at)
        self.assertEqual(self.model.__dict__, model2.__dict__)

    def test_kwargs_type(self):
        """Test kwargs type"""
        model_dict = self.model.to_dict()
        model2 = BaseModel(**model_dict)
        self.assertEqual(type(model2.id), str)
        self.assertEqual(type(model2.created_at), datetime)
        self.assertEqual(type(model2.updated_at), datetime)

    def test_kwargs_format(self):
        """Test kwargs format"""
        model_dict = self.model.to_dict()
        model2 = BaseModel(**model_dict)
        self.assertEqual(model2.__dict__, self.model.__dict__)

    def test_kwargs_none(self):
        """Test kwargs none"""
        model2 = BaseModel()
        model2.save()
        model2_dict = model2.to_dict()
        model3 = BaseModel(**model2_dict)
        self.assertEqual(model2.id, model3.id)
        self.assertEqual(model2.created_at, model3.created_at)
        self.assertEqual(model2.updated_at, model3.updated_at)
        self.assertEqual(model2.__dict__, model3.__dict__)

    def test_kwargs_one(self):
        """Test kwargs one"""
        model2 = BaseModel()
        model2.save()
        model2_dict = model2.to_dict()


if __name__ == '__main__':
    unittest.main()
