#!/usr/bin/env python3
""" Duck type an iterable object """
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ """
    return [(i, len(i)) for i in lst]
