#!/usr/bin/env python3
""" Validate type checking """
from typing import Tuple, Union, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zoom array implementation """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
