#!/usr/bin/env python3
"""Uniitest mock modules"""
import unittest
from unittest.mock import patch
from clien import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGuthubOrgClient class"""
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        """Tests that client returns correct value"""
        url = "https://api.github.com/orgs/{}".format(name)
        test = GithubOrgClient(name)
        test.org()
        mock.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Method testing for public repo"""
        with patch('client.GithubOrgClient.org'
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test = GithubOrgClient('test')
            result = test._public_repos_url
            self.assertEqual(payload["repos_url"])
