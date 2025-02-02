#!/usr/bin/env python3
"""web cache and tracker"""
import redis
import requests


cache = redis.Redis()


def get_page(url: str) -> str:
    """gets a page and track requests"""
    cache.incr('count:{}'.format(url))
    if cache.get('count:{}'.format(url)):
        return cache.get('count:{}'.format(url))
    req = requests.get(url)
    cache.setex('count:{}'.format(url), 10, req.text)
    return req.text
