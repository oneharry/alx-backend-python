#!/usr/bin/env python3
""" Complex types - function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that takes a float args.
    return the multiple of the arg"""

    def callable_multiplier(x: float) -> float:
        """returns the multiple of the paramter x"""
        return x * x

    return callable_multiplier
