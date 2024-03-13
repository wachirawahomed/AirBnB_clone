#!/usr/bin/env python3
"""Unittest for State model"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test instance attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
