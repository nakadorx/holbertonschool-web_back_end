#!/usr/bin/env python3
"""holb"""

import requests


def get_page(url: str) -> str:
    """holb
    """
    req = requests.get(url)
    return req.content
