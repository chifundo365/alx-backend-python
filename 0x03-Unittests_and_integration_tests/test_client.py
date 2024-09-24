#!/usr/bin/env python3
''' Tests an API '''
import unittest
from unittest.mock import patch
from parameterized import parameterized
import client



class TestGithubOrg(unittest.TestCase):
    ''' Test class for the GithubOrgClient '''

    @parameterized.expand(
            [
                ("google",),
                ("abc",)
            ]
    )
    @patch('client.get_json')
    def test_org(self, org, mock):
        ''' Self descriptive '''
        endpoint =  'https://api.github.com/orgs/{}'.format(org)
        spec = client.GithubOrgClient(org)
        spec.org()
        mock.assert_called_once_with(endpoint)

if __name__ == "__main__":
    unittest.main()
