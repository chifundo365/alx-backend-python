#!/usr/bin/env python3
''' Implements and annotates a function "sum_mixed_list" '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    calculates the sum of floats and int

    Args:
        mxd_lst: List of floats and ints
    Returns:
        float: sum of the numbers
    '''
    return sum(mxd_lst)
