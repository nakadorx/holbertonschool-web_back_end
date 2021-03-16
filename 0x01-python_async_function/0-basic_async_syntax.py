#!/usr/bin/env python3
"""holb"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait
    """
    randomized = random.uniform(0, max_delay)
    await asyncio.sleep(randomized)
    return randomized