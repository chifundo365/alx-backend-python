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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        ''' unit tests public_repos '''
        payload = [{'name': 'Google'}, {'name': 'Apple'}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                  new_callable=PropertyMock
                  ) as mocked_public:
            
            mocked_public.return_value = 'https://world.com'
            res = client.GithubOrgClient('name').public_repos()

            self.assertEqual(res, ['Google', 'Apple'])

            mocked_public.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
