#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum float and int together

    Args:
        mxd_lst (List[float, int]): List of float and int

    Return:
        (float): sum of the list
    """
    return float(sum(mxd_lst))
