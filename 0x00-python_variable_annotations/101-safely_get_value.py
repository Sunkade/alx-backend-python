#!/usr/bin/env python3
"""
Module: 101-safely_get_value

Contains a function safely_get_value that retrieves a value from a dictionary safely.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value corresponding to the given key from the dictionary.
    
    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Optional[T], optional): The default value to return if the key is not found. Defaults to None.
    
    Returns:
        Union[Any, T]: The value corresponding to the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
