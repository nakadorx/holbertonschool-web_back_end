#!/usr/bin/env python3
"""holb
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """holb
    """
    return (page * page_size - page_size, page * page_size)
