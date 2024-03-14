#!/usr/bin/env python3

"""
type-annotated function
"""


import math

def floor(n: float) -> int:
    """
    returns floor of a float
    """
    res: int = math.floor(n)
    return res
