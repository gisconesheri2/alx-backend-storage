#!/usr/bin/env python3
"""
use a redis client to store a value to the database
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache():

    def __init__(self):
        """create a new instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in a redis server"""
        k_str = str(uuid.uuid4())
        self._redis.set(k_str, data)
        return k_str
    
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, float, str, bytes]:
        """get the value associated with key"""
        val = self._redis.get(key)
        if val:
            if fn:
                return fn(val)
            else:
                return val
        return val
    
    def get_str(self, key: str) -> str:
        """
        convert value from the database
        into a string
        """
        val = self._redis.get(key)
        if val:
            val.decode('utf-8')
        return val
    
    def get_int(self, key: str) -> Union[int, None]:
        """
        convert value from the database
        into an integer
        """
        val = self._redis.get(key)
        if val:
            try:
                val = int(val.decode('utf-8'))
            except ValueError:
                val = None
        return val
