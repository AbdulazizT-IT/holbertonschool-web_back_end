#!/usr/bin/env python3
"""
This module provides a function to compute the sum of
a list containing both integers and floating-point numbers.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number (int or float), returns a tuple with
    the string and the square of the number as a float.

    Args:
        k (str): The key string.
        v (int or float): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple where
        the first element is the key,
        and the second element is the squared value as float.
    """
    return (k, float(v ** 2))
