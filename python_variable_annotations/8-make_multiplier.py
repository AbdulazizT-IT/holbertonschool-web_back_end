#!/usr/bin/env python3
"""
This module provides a function to compute the sum of
a list containing both integers and floating-point numbers.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The number to multiply by.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the product.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
