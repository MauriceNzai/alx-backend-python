#!/usr/bin/env python3

"""
type-annotated function
"""


def concat(str1: str, str2: str) -> str:
    """
    returns concatenated string str1 and str2
    """
    res: str = str1 + str2
    return res
