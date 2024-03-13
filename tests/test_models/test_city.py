#!/usr/bin/python3
"""Unittest for City Model"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test instance attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
