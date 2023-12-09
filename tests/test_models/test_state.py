#/usr/bin/python3
"""test state class"""
import unittest
from models.base_model import BaseModel
from moodels.state import State


class TestState(unittest.TestCase):
    """test state class"""
    def test_state(self):
        """test of state"""
        obj = State()
        self.assertEqual(isinstance(obj, BaseModel), True)
        self.assertEqual(isinstance(obj, State), True)
        self.assertEqual(obj.__class__.__name__, 'State')
        self.assertEqual(type(obj.name), str)

if __name__ == '__main__':
    unittest.main()
