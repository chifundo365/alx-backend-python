#!/usr/bin/env python3
''' Tests an API '''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client



class TestGithubOrgClient(unittest.TestCase):
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

    @parameterized.expand([
        ('random_url', {'repos_url': 'https://some_url.com'})
        ])
    def test_public_repos_url(self, name, result):
        ''' Tests public_repos_url '''
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = result
            res = client.GithubOrgClient(name)._public_repos_url
            self.assertEqual(res, result.get('repos_url'))


if __name__ == "__main__":
    unittest.main()
