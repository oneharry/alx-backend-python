#!/usr/bin/env python3
""" Basics of async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Function waits for max_delay, returns the the value """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
