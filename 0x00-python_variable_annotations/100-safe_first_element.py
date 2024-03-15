#!/usr/bin/env python3
"""
Module: 100-safe_first_element

Contains a function safe_first_element that returns the first element of a sequence safely.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the given sequence if it exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
