#!/usr/bin/env python3

"""
type-annotated function
"""


def add(a: float, b: float) -> float:
    """
    returns sum of a and b as float
    """
    res: float = a + b
    return res
