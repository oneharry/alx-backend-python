#!/usr/bin/ebn python3
""" Async Comprehension """
import asyncio
from typing import Iterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterable[float]:
    """ Collect random number from func, returns random num"""
    return [item async for item in async_generator()]
