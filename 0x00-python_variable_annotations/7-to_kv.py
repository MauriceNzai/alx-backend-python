#!/usr/bin/env python3

"""
type-annotated function to return atuple
"""

from typing import Union, Tuple
def to_kv(k: str, v: Union[float, int])-> Tuple[str, float]:
    """
    returns tuple from the args
    """
    res: Tuple(str, float) = (k, float(v ** 2))
    return res
