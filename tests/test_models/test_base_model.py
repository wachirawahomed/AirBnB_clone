#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        self.assertEqual(
            str(my_model),
            "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        )

    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue('__class__' in my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in my_model_dict)
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertTrue('created_at' in my_model_dict)
        self.assertEqual(
            my_model_dict['created_at'],
            my_model.created_at.isoformat()
        )
        self.assertTrue('updated_at' in my_model_dict)
        self.assertEqual(
            my_model_dict['updated_at'],
            my_model.updated_at.isoformat()
        )

    def test_custom_attributes(self):
        my_model = BaseModel()
        my_model.my_number = 89
        self.assertTrue(hasattr(my_model, 'my_number'))
        self.assertEqual(my_model.my_number, 89)

if __name__ == "__main__":
    unittest.main()
