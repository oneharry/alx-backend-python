#!/usr/bin/env python3
"""Uniitest mock modules"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from clien import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixture import TEST_PAYLOAD
import json


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

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """test taht list of repos is what is expected in function get_json
        Test that mocked property and method is called once"""
        payload = [{"name": "Google"}, {"name": "Twitter"}]

        with patch('client.GithubOrgClient._public_repos_url'
                   new_callable=PropertyMock) as repo_mock:
            repo_mock .return_value = "hello/world"
            test = GithubOrgClient('test')
            result = test.public_repos()

            data_list = [x["name"] for x in payload]
            self.assertEqual(data_list, result)

            mock.assert_called_once()
            repo_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_licence(self, repo, licence_key, expected):
        """test for has_licence"""
        result = GithubOrgClient.has_licence(repo, licence_key)
        self.assertEqual(result, expected)


@parameterized_class('org_payload', 'repos_payload', 'expected_repos',
                     'apache2_repos', TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """Set up method for all tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock = cls.get_patcher.start()

        cls.mock.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """ Tear down, called at the end of all tests"""
        cls.get_patcher.stop()

    @patch('client.GithubOrgClient.get_json')
    def test_public_repos(self, mock):
        """Test publiv repos"""

        mock.side_effect = [org_payload, repos_payload]
        name = "google"
        test = GithubOrgClient(name)

        pub_repo = client.public_repos

        expected_org_url = f'https://api.github.com/orgs/{org_name}'
        expected_repos_url = f'https://api.github.com/orgs/{org_name}/repos?
                              license=apache-2.0'
        mock.assert_called_with(expected_org_url)
        mock.assert_called_with(expected_repos_url)

        self.assertEqual(pub_repo, expected_repos)

    @patch('client.GithubOrgClient.get_json')
    def test_repos_with_licence(self, mock):
        """testing integration for repos with licencs"""
        mock.side_effect = [org_payload, apache2_repos]
        name = "google"
        test = GithubOrgClient(name)
        pub_repo = client.public_repos(license="apache-2.0")

        expected_org_url = f'https://api.github.com/orgs/{org_name}'
        expected_repos_url = f'https://api.github.com/orgs/{org_name}/repos?
                              license=apache-2.0'
        mock.assert_called_with(expected_org_url)
        mock.assert_called_with(expected_repos_url)

        self.assertEqual(pub_repo, apache2_repos)

