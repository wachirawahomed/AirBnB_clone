#!/usr/bin/env python3
"""Unittest for Review Model"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test instance attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
