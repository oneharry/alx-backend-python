#!/usr/bin/env python3
""" Parametzise unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test exception raised from nested map"""
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(exc.exception), f"KeyError('{expected}')")


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json"""
        conf = {'return_value.json.return_value': test_payload}
        json_patch = patch('requests.get', **conf)
        mock = json_patch.start()
        mock.asser_called_once()
        json_patch.stop()


class TestMemoize(unittest.TestCase):
    """ TestMemoize class"""

    def test_memoize(self):
        """ Test that a memoized function a_method is call once when
        a_property is called twice"""

        class TestClass:
            """ TestClass class for memoization"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
