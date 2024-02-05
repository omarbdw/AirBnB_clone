#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test instantiation of Place class with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of Place is stored in __objects attr."""
        self.assertIn(Place(), Place._FileStorage__objects.values())

    def test_id_is_public_str(self):
        """Test that id attribute is a public class attribute and is a str."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at attribute is public and is a datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that updated_at attribute is public and is a datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_user_id_is_public_str(self):
        """Test that user_id attribute is public and is a str."""
        self.assertEqual(str, type(Place().user_id))

    def test_city_id_is_public_str(self):
        """Test that city_id attribute is public and is a str."""
        self.assertEqual(str, type(Place().city_id))

    def test_name_is_public_str(self):
        """Test that name attribute is public and is a str."""
        self.assertEqual(str, type(Place().name))

    def test_description_is_public_str(self):
        """Test that description attribute is public and is a str."""
        self.assertEqual(str, type(Place().description))

    def test_number_rooms_is_public_int(self):
        """Test that number_rooms attribute is public and is an int."""
        self.assertEqual(int, type(Place().number_rooms))

    def test_number_bathrooms_is_public_int(self):
        """Test that number_bathrooms attribute is public and is an int."""
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_max_guest_is_public_int(self):
        """Test that max_guest attribute is public and is an int."""
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night_is_public_int(self):
        """Test that price_by_night attribute is public and is an int."""
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude_is_public_float(self):
        """Test that latitude attribute is public and is a float."""
        self.assertEqual(float, type(Place().latitude))

    def test_longitude_is_public_float(self):
        """Test that longitude attribute is public and is a float."""
        self.assertEqual(float, type(Place().longitude))


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    def test_save_updates_updated_at(self):
        """Test that save method updates the updated_at attribute."""
        inst = Place()
        old_updated_at = inst.updated_at
        sleep(0.1)
        inst.save()
        self.assertLess(old_updated_at, inst.updated_at)

    def test_save_updates_updated_at_filestorage(self):
        """Test that save method updates the updated_at
        attribute in storage."""
        inst = Place()
        old_updated_at = inst.updated_at
        sleep(0.1)
        inst.save()
        key = inst.__class__.__name__ + '.' + inst.id
        self.assertLess(
            old_updated_at, Place._FileStorage__objects[key].updated_at)

    def test_save_saves_to_file(self):
        """Test that save method saves updated object to file"""
        inst = Place()
        key = inst.__class__.__name__ + '.' + inst.id
        os.remove("file.json")
        inst.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r") as f:
            self.assertIn(key, json.load(f))

    def test_save_saves_to_file_filestorage(self):
        """Test that save method saves updated object to filestorage"""
        inst = Place()
        key = inst.__class__.__name__ + '.' + inst.id
        os.remove("file.json")
        inst.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r") as f:
            self.assertIn(key, json.load(f))

    def test_save_no_args(self):
        """Test that save method has no args"""
        with self.assertRaises(TypeError):
            Place.save()


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test type of return from to_dict method."""
        inst = Place()
        self.assertEqual(dict, type(inst.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test keys in to_dict dictionary."""
        inst = Place()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test keys in to_dict dictionary."""
        inst = Place()
        inst.name = "Holberton"
        inst.number = 98
        self.assertIn("name", inst.to_dict())
        self.assertIn("number", inst.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test datetime values in dictionary are str type."""
        inst = Place()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst_dict = inst.to_dict()
        self.assertEqual(str, type(inst_dict["created_at"]))
        self.assertEqual(str, type(inst_dict["updated_at"]))
        self.assertEqual(time_format, inst_dict["created_at"])
        self.assertEqual(time_format, inst_dict["updated_at"])
        self.assertEqual("Place", inst_dict["__class__"])

    def test_to_dict_output_no_args(self):
        """Test output of to_dict with no args."""
        inst = Place()
        with self.assertRaises(TypeError):
            inst.to_dict(1)

    def test_to_dict_output_extra_arg(self):
        """Test output of to_dict with extra arg."""
        inst = Place()
        with self.assertRaises(TypeError):
            inst.to_dict("test")

    def test_to_dict_output_kwargs(self):
        """Test output of to_dict with kwargs."""
        inst = Place()
        with self.assertRaises(TypeError):
            inst.to_dict(key="test")

    def test_to_dict_output_more_than_one_arg(self):
        """Test output of to_dict with more than one arg."""
        inst = Place()
        with self.assertRaises(TypeError):
            inst.to_dict(1, 2)


if __name__ == '__main__':
    unittest.main()
