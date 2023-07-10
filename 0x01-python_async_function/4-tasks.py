#!/usr/bin/env python3
""" Multiple coroutines """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Executes wait_random n-times with max_delay as argument
        Returns a sorted list without using the sort method
    """
    wait_list = [task_wait_random(max_delay) for _ in range(n)]

    return [await item for item in asyncio.as_completed(wait_list)]
