#!/usr/bin/python3
"""test amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test amenity class"""
    def test_amenity(self):
        """test of amenity"""
        obj = Amenity()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, Amenity), True)
        self.assertEqual(type(obj.name), str)

if __name__ == '__main__':
    unittest.main()
