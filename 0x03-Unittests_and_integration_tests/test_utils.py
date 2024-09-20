#!/usr/bin/env python3
""" Unit Testing a function """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict, Any
from utils import access_nested_map


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
                ({}, ("a",), KeyError, 'a'),
                ({"a": 1}, ("a", "b"), KeyError, 'b')
            ])
    def test_acces_mested_map_exception(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str],
            expected: Any,
            error_key: str
            ):
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], str(error_key))


if __name__ == "__main__":
    unittest.main()
