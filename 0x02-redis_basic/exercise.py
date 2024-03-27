#!/usr/bin/env python3
"""
use a redis client to store a value to the database
"""
import redis
import uuid
from typing import Union


class Cache():

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        k_str = str(uuid.uuid4())
        self._redis.set(k_str, data)
        return k_str
