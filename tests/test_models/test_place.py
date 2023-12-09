#!/usr/bin/python3
"""test Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """test Place class"""
    def test_place(self):
        """test of Place"""
        obj = Place()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, Place), True)
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.description), str)
        self.assertEqual(type(obj.city_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.amenity_ids), list)
        self.assertEqual(type(obj.number_rooms), int)
        self.assertEqual(type(obj.number_bathrooms), int)
        self.assertEqual(type(obj.max_guest), int)
        self.assertEqual(type(obj.price_by_night), int)
        self.assertEqual(type(obj.latitude), float)
        self.assertEqual(type(obj.longitude), float)


if __name__ == '__main__':
    unittest.main()
