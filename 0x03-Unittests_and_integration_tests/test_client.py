#!/usr/bin/env python3
"""
Familiarize yourself with the client.GithubOrgClient class.

In a new test_client.py file, declare the TestGithubOrgClient
(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the
expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a
couple of org examples to pass to GithubOrgClient, in this order:

google
abc
Of course, no external HTTP calls should be made
"""

import client
import requests
import unittest
import utils
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock, call
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """
    tests that GithubOrgClient.org returns the correct value
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        tests that GithubOrgClient.org returns
        """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """
        test that _public_repos_url works
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            client = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)
