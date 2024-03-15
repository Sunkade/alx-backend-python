#!/usr/bin/env python3
"""
Module: 102-type_checking

Contains a function to zoom in on a tuple by repeating each element a certain number of times.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """
    Zooms in the given tuple by repeating each element a certain number of times.

    Args:
        lst (Tuple[int]): The input tuple to be zoomed in.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple[int]: The zoomed-in tuple.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)
