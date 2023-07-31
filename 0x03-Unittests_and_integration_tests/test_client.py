#!/usr/bin/env python3
"""Uniitest mock modules"""
import unittest
from unittest.mock import patch
from clien import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGuthubOrgClient class"""
    @patch('client.get_json')
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    def test_org(self, name, mock):
        """Tests that client returns correct value"""
        url = "https://api.github.com/orgs/{}".format(name)
        test = GithubOrgClient(name)
        test.org()
        mock.assert_called_once_with("{}".format(url))
