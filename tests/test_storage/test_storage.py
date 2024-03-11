#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test all method of FileStorage"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method of FileStorage"""
        self.storage.new(self.base_model)
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method of FileStorage"""
        self.storage.new(self.base_model)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertIn(self.base_model.__class__.__name__, data)
            self.assertIn(self.base_model.id, data)

    def test_reload(self):
        """Test reload method of FileStorage"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
