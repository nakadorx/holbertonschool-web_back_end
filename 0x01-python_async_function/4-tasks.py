#!/usr/bin/env python3
"""holbd"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """holbd"""
    covid = (task_wait_random(max_delay) for i in range(n))
    l = await asyncio.gather(*covid)
    return sorted(l)
 