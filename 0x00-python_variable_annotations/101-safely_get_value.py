#!/usr/bin/env python3
"""More Type annotations """
from typing import TypeVar, Dict, Any, Union, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """ Implement more type annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
