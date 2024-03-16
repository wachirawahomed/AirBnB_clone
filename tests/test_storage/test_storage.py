#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User(email="test@example.com", password="password")
        self.state = State(name="California")
        self.city = City(name="San Francisco", state_id=self.state.id)
        self.amenity = Amenity(name="Wifi")
        self.place = Place(name="Cozy Apartment",
                           city_id=self.city.id,
                           user_id=self.base_model.id)
        self.review = Review(text="Great place to stay",
                             place_id=self.place.id,
                             user_id=self.user.id)

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test all method of FileStorage"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_instance_creation(self):
        """Test creation of new instances"""
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)

        self.assertTrue(len(self.storage.all()), 7)

    def test_save_and_reload(self):
        """Test save and reload methods"""
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        # Check if all objects were reloaded correctly
        self.assertIn("BaseModel.{}".format(self.base_model.id),
                      new_storage.all())
        self.assertIn("User.{}".format(self.user.id), new_storage.all())
        self.assertIn("State.{}".format(self.state.id), new_storage.all())
        self.assertIn("City.{}".format(self.city.state_id), new_storage.all())
        self.assertIn("Amenity.{}".format(self.amenity.id), new_storage.all())
        self.assertIn("Place.{}".format(self.place.id), new_storage.all())
        self.assertIn("Review.{}".format(self.review.id), new_storage.all())


if __name__ == '__main__':
    unittest.main()
