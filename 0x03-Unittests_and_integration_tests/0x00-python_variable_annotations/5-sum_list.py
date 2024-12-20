#!/usr/bin/env python3
"""Write a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum list of float

    Args:
        input_list (List[float]): List of float

    Return
        (float): sum of all element
    """
    sum = 0
    for item in input_list:
        sum += item

    return sum
