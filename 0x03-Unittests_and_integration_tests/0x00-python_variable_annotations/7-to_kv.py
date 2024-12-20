#!/usr/bin/env python3
"""Write a type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert str and int/float into key and value tuple

    Args:
        k (str): key
        v (Union[int, float]): value

    Return:
        (Tuple): key and value pairs
    """
    return (k, v**2)
