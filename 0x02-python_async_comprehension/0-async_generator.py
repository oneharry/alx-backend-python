#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loops 10 time, yield a random number after waiting 1 sec"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
