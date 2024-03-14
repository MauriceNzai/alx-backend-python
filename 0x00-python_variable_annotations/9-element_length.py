#!/usr/bin/env python3

"""
Type annotations
"""

from typing import Iterable, List, Sequence, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    type annotated function
    """
    return [(i, len(i)) for i in lst]
