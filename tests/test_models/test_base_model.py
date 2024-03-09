#!/usr/bin/python3
import uuid
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        # Test if id is a string
        self.assertIsInstance(self.model.id, str)

        # Test if id is a valid UUID
        try:
            uuid_obj = uuid.UUID(self.model.id)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        # Save the model and check if updated_at changed
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)

        # Check for expected keys in the dictionary
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, model_dict)

        # Check if the datetimes are formatted correctly
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs_initialization(self):
        # Test initialization with kwargs
        test_id = "test_id"
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        kwargs = {
            'id': test_id,
            'created_at': created_at,
            'updated_at': updated_at,
            'name': 'Test Model'
        }
        model_with_kwargs = BaseModel(**kwargs)
        self.assertEqual(model_with_kwargs.id, test_id)
        self.assertEqual(model_with_kwargs.created_at.isoformat(), created_at)
        self.assertEqual(model_with_kwargs.updated_at.isoformat(), updated_at)
        self.assertTrue(hasattr(model_with_kwargs, 'name'))


if __name__ == '__main__':
    unittest.main()
