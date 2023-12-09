#/usr/bin/python3
"""test Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """test state class"""
    def test_Review(self):
        """test of state"""
        obj = Review()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, Review), True)
        self.assertEqual(obj.__class__.__name__, 'Review')
        self.assertEqual(type(obj.text), str)
        self.assertEqual(type(obj.place_id), str)
        self.assertEqual(type(obj.user_id), str)

if __name__ == '__main__':
    unittest.main()
