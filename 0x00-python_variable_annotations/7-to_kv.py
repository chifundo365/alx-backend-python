#!/usr/bin/env python3
''' Implements a typ-annotated function "to_kv" '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Union[Tuple[str, float]]:
    '''
    Returns a tuple of a strin and a suquared number(v)
    '''
    return k, v * v
