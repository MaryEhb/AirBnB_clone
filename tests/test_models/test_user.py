#!/usr/bin/python3
"""test User class"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """test User class"""
    def test_user(self):
        """test of User"""
        obj = User()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, User), True)
        self.assertEqual(type(obj.email), str)
        self.assertEqual(type(obj.password), str)
        self.assertEqual(type(obj.first_name), str)
        self.assertEqual(type(obj.last_name), str)

if __name__ == '__main__':
    unittest.main()
