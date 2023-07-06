#!/usr/bin/env python3
"""Complex types - Tuple of list and float """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple of string and int or float """
    return (k, v * v)
