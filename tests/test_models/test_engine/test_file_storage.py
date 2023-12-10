#/usr/bin/python3
"""test state class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
from models import storage

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
        pass

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        pass

if __name__ == '__main__':
    unittest.main()
