#!/usr/bin/env python3
"""
use a redis client to store a value to the database
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count number of times a function is called"""

    @wraps(method)
    def increment_call(self, *args, **kwargs):
        """Increments the value associated with methond name"""
        self._redis.incr(method.__qualname__, amount=1)
        return method(self, *args, **kwargs)
    return increment_call


def call_history(method: Callable) -> Callable:
    """add inputs and outputs of method to
    method's respective fields"""

    m_inp = "{}:inputs".format(method.__qualname__)
    m_out = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def add_args(self, *args, **kwargs):
        """push to funtion inputs and outputs fields"""

        self._redis.rpush(m_inp, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(m_out, str(out))
        return out
    return add_args


def replay(method: Callable) -> None:
    r = redis.Redis()
    mn = method.__qualname__
    calls = r.get(mn)
    print('{} was called {} times:'.format(mn, calls))

    inputs =r.lrange("{}:inputs".format(mn), 0, -1)
    outputs = r.lrange("{}:outputs".format(mn), 0, -1)
    io = zip(inputs, outputs)
    
    for i, o in io:
        i_str = i.decode('utf-8')
        o_str = o.decode('utf-8')
        print('{}(*({})) -> {}'.format(mn, i_str, o_str))


class Cache():

    def __init__(self):
        """create a new instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
