#!/usr/bin/env python3
""" Unit Testing a function """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict, Any
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Run dedicated tests """
    @parameterized.expand(
            [

                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
            ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any
            ) -> None:
        """ tests with the right paramiterised inputs  and expected output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
            [
                ({}, ("a",), KeyError),
                ({"a": 1}, ("a", "b"), KeyError)
            ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str],
            expected: Any,
            ):
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests for the utils.get_json method """
    @parameterized.expand(
            [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payloas": False})
            ])
    @patch("utils.requests.get")
    def test_get_json(self, url, expected_response, mock_get):
        """ tests for the get_json method(Mocked)"""
        mock_get.return_value.json.return_value = expected_response
        res = get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(res, expected_response)


class TestMemoize(unittest.TestCase):
    """ Tests memoization """
    def test_memoize(self):
        ''' tests for the memoize method '''
        class TestClass:

            def a_method(self):
                ''' a_ method returns 42 '''
                return 42

            @memoize
            def a_property(self):
                '''returns self.a_method'''
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
