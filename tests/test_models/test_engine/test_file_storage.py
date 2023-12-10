#/usr/bin/python3
"""test state class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestEngine(unittest.TestCase):
    """test file storage class"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_storage(self):
        self.assertEqual(type(storage), FileStorage)

    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_path_type_str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_obj_type_dict(self):
         self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_new_none(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_new_base_model(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_user_model(self):
        obj = User()
        storage.new(obj)
        self.assertIn("User." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_review_model(self):
        obj = Review()
        storage.new(obj)
        self.assertIn("Review." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_city_model(self):
        obj = City()
        storage.new(obj)
        self.assertIn("City." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_place_model(self):
        obj = Place()
        storage.new(obj)
        self.assertIn("Place." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_state_model(self):
        obj = State()
        storage.new(obj)
        self.assertIn("State." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_new_amenity_model(self):
        obj = Amenity()
        storage.new(obj)
        self.assertIn("Amenity." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

    def test_save_base_model(self):
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("BaseModel." + obj.id, file_content)

    def test_save_user_model(self):
        obj = User()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("User." + obj.id, file_content)

    def test_save_city_model(self):
        obj = City()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("City." + obj.id, file_content)

    def test_save_state_model(self):
        obj = State()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("State." + obj.id, file_content)

    def test_save_Place_model(self):
        obj = Place()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("Place." + obj.id, file_content)

    def test_save_review_model(self):
        obj = Review()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("Review." + obj.id, file_content)

    def test_save_amenity_model(self):
        obj = Amenity()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("Amenity." + obj.id, file_content)

    def test_reload(self):
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + obj.id, objs)



if __name__ == '__main__':
    unittest.main()
