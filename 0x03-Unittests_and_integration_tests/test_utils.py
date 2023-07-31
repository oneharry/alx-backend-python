#!/usr/bin/env python3
""" Parametzise unit test"""
import unittest
from parametized import parametized
from utils import (access_nested_map, get_json, memoize)
from unittest.mock import patch


class TestAccessNestesdMap(unittest.TestCase):
    """test class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that method returns accordingly"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
