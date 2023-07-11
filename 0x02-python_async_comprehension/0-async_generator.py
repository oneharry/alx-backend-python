#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
from typing import Iterable


async def async_generator() -> Iterable[float]:
    """ Loops 10 time, yield a random number after waiting 1 sec"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)