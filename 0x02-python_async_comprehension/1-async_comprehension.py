#!/usr/bin/env python3
"""[async_gen]
"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[async_gen]

    a:
        a[fint: [a]
    """
    return [num async for num in async_generator()]
