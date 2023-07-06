#!/usr/bin/env python3
""" Complex annotations type - Mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns sum of interges and floats in a list as float"""
    sum_total: float = 0
    for item in mxd_list:
        sum_total += item

    return sum_total
