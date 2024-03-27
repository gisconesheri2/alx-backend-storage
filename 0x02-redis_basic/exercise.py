#!/usr/bin/env python3
"""
use a redis client to store a value to the database
"""
from __init__ import _redis as r
import uuid
from typing import Union


class Cache():

    def store(data: Union[str, bytes, int, float]) -> str:
        k_str = str(uuid.uuid4())
        r.set({k_str: data})
        return k_str
