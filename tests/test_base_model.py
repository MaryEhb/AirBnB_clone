#!/usr/bin/python3
"""Unit Testing for Base Model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel Class"""

    def test_no_args(self):
        """Test BaseModel initialization with no arguments"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_with_args(self):
        """Test BaseModel initialization with arguments"""
        obj = BaseModel(id="123", created_at="2023-01-01T12:00:00.000000",
                        custom_attr="value")
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.custom_attr, "value")

    def test_created_updated_type(self):
        """Test types of created_at and updated_at attributes"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_ids(self):
        """Test that generated IDs are unique"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_update_same_as_created(self):
        """
        Test that updated_at is the same as created_at
        during object initialization
        """
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_updated_after_created(self):
        """
        Test that updated_at is different and after
        created_at after calling save
        """
        obj = BaseModel()
        created_time = obj.created_at
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertGreater(obj.updated_at, created_time)

    def test_none_arg(self):
        """Test BaseModel initialization with None argument"""
        obj = BaseModel(None)
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_values(self):
        """Test if to_dict() returns dictionary with correct values"""
        obj = BaseModel(id="123", created_at="2023-01-01T12:00:00.000000",
                        custom_attr="value",
                        updated_at="2023-01-01T12:00:00.000000")
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], "123")
        self.assertEqual(obj_dict['custom_attr'], "value")
        self.assertEqual(obj_dict['__class__'], "BaseModel")
