#!/usr/bin/env python3
"""
This module provides a function to compute the sum of
a list containing both integers and floating-point numbers.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and/or floating-point numbers.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of numeric values (integers and floats).

    Returns:
    float: The total sum of the values in the list as a floating-point number.
    """
    return sum(mxd_lst)
    