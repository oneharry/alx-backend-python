#!/usr/bin/env python3
""" Multiple coroutines """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Executes wait_random n-times with max_delay as argument
        Returns a sorted list without using the sort method
    """
    wait_list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await item for item in asyncio.as_completed(wait_list)]
