#!/usr/bin/env python3
''' Defines a duck-typed function '''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
