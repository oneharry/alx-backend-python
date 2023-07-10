#!/usr/bin/env python3
""" Basics of async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Function waits for max_delay, returns the the value """
    await asyncio.sleep(max_delay)
    if max_delay < 0:
        return random.uniform(max_delay, 0)
    return random.uniform(0, max_delay)
