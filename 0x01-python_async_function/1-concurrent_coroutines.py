#!/usr/bin/env python3
""" Multiple coroutines """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """ Executes wait_random n-times with max_delay as argument
        Returns a sorted list without using the sort method
    """
    wait_list = [await wait_random(max_delay) for i in range(n)]

    return sorted(wait_list)
