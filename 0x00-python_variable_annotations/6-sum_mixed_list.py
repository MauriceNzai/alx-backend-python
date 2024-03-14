#!/usr/bin/env python3

"""
type-annotated function to sum list of mixed values
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """
    returns sum of list elements
    """
    res: float = sum(mxd_list)
    return res
