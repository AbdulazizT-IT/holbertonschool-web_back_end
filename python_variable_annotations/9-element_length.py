#!/usr/bin/env python3


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element and its length
    from an iterable of sequences.

    Args:
        lst: An iterable containing elements that
        support len() (e.g., list, str, tuple).

    Returns:
        A list of tuples, each containing
        the element and its length.
    """
    return [(i, len(i)) for i in lst]