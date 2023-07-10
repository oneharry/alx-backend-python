#!/usr/bin/env python3
""" Measure runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure and return the total time of execution """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
