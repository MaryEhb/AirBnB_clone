#!/usr/bin/python3
"""test city class"""
import unittest
from models.base_model import BaseModel
from models.city import City

class TestState(unittest.TestCase):
    """test state class"""
    def test_city(self):
        """test of city"""
        obj = City()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, City), True)
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.state_id), str)

if __name__ == '__main__':
    unittest.main()
