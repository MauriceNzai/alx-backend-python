#!/usr/bin/env python3

"""
type-annotated function to sum list values
"""

from typing import List
def sum_list(input_list: List[float])-> float:
    """
    returns sum of list elements
    """
    res: float = sum(input_list)
    return res
