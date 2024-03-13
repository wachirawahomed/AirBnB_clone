#!/usr/bin/python3
"""Unit Test for The User Class"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User(email="test@example.com", password="password")

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_email_password(self):
        """Test email and password attributes"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")


if __name__ == '__main__':
    unittest.main()
