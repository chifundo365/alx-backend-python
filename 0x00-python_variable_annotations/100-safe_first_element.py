#!/usr/bin/env python3
''' Defines a duck-typed function '''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    '''
    Returns the first item of an iterable or None if lst id not iterable
    '''
    if lst:
        return lst[0]
    else:
        return None
