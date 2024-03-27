#!/usr/bin/env python3
"""Cache results"""

from functools import wraps
import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ decorator for counting url access """

    @wraps(method)
    def count_access(url):
        """ Wrapper for decorator """
        redis_client.incr(f"count:{url}", amount=1)
        html_cache = redis_client.get(f"cached:{url}")
        if html_cache:
            return html_cache.decode('utf-8')
        html = method(url)
        redis_client.set(f"cached:{url}", html, ex=10)
        return html

    return count_access


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a given URL """
    resp = requests.get(url)
    return resp.text
