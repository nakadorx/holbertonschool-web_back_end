#!/usr/bin/env python3
"""[async_gen]
"""

from typing import List
from time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[async_gen]

    a:
        a[fint: [a]
    """
    counter = perf_counter()
    task_list = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*task_list)
    elapsed_time = perf_counter() - counter
    return elapsed_time
