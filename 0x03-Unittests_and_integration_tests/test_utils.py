#!/usr/bin/env python3
""" Unit Testing a function """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccsesNestedMap(unittest.TestCase):
    """ Run dedicated tests """
    @parameterised.expand(
            [

                (nested_map={"a": 1}, path=("a",), 1)
                (nested_map={"a": {"b": 2}}, path=("a",), {"b": 2})
                (nested_map={"a": {"b": 2}}, path=("a", "b"), 2)
            ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ tests with different paramiterised input """
        assert_equal(access_nested_map(nested_map, path), expected)
