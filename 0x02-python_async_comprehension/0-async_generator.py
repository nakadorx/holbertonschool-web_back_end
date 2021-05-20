#!/usr/bin/env python3
"""[async_gen]
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """[async_gen]

    a:
        a[fint: [a]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10