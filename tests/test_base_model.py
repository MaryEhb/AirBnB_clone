#!/usr/bin/python3
"""Unit Testing for Base Model"""
import unittest


class TestBaseModel(unittest.TestCase):
    """TestBase Class"""

    # check no args
    # check with args
    # check created type === datetime obj
    # check update type === datetime
    # check that ids are unique
    # update is the same as created when obg init
    # updated_at is diff and after created_at when obj save
    # None arg
    # check to_dict() values the same as model values
