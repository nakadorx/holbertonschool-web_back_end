#!/usr/bin/env python3
"""holb"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """holb"""
    ctrB = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    ctrA = time.perf_counter()
    return (ctrA - ctrB) / n
