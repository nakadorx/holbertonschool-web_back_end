#!/usr/bin/env python3
"""[holb]
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """holb
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """holb
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)