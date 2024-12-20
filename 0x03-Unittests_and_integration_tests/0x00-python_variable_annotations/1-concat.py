#!/usr/bin/env python3
"""Write a type-annotated function concat"""


def concat(str1: str, str2: str) -> str:
    """Concatenate two strings

    Args:
        str1 (str): First string
        str2 (str): Second string

    Return:
        (str) - concatenated string
    """
    return ''.join([str1, str2])
    # return str1 + str2
