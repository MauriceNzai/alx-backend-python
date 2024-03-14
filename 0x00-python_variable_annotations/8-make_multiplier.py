#!/usr/bin/env python3

"""
type-annotated function to return a function
"""

from typing import Callable

def make_multiplier(multiplier: float)-> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
