#!/usr/bin/env python3
"""
Module: 100-safe_first_element

Contains a function safe_first_element that returns the first element of a sequence safely.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    
    if lst:
        return lst[0]
    else:
        return None


