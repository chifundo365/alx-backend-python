#!/usr/bin/env python3
''' implements a type-annotated function '''
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list with a tuple inside it
    '''
    return [(i, len(i)) for i in lst]
