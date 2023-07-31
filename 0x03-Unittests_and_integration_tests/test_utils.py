#!/usr/bin/env python3
""" Parametzise unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """testAccessNestedMap class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that method returns accordingly"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
