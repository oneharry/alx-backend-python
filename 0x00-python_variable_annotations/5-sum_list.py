#!/usr/bin/python3
""" Complex annotations types - list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns sum of floats of list """
    sum_float: float = 0
    for item in input_list:
        sum_float += item

    return sum_float
