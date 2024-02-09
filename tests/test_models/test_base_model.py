#!/usr/bin/python3
"""This module contains a test for class BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """creates tests that test all instances and
    methods of class BaseModel"""

    def setUp(self):
        """sets up the values of BaseModel each time the tests are ran"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        """Tears down the values after each test is done"""
        del self.my_model

    def test_attributes(self):
        """Tests the atttributes of the BaseModel"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertTrue(hasattr(self.my_model, '__str__'))
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertTrue(hasattr(self.my_model, 'to_dict'))


if __name__ == "__main__":
    unittest.main()