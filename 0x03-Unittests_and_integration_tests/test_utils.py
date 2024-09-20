#!/usr/bin/env python3
""" Unit Testing a function """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict, Any
from utils import access_nested_map


class TestAccsesNestedMap(unittest.TestCase):
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
        """ tests with different paramiterised input """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
