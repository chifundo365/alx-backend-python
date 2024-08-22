#!/usr/bin/env python3
''' Defines a type-annotated function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that multipliers a float by the multiplier
    '''
    def multiplier_func(f: float) -> float:
        return multiplier * f

    return multiplier_func
