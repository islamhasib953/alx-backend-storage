#!/usr/bin/env python3

""" Task1 exercise """

import redis, uuid
from typing import Union, Callable, Optional
from functools import wraps


def replay(method: Callable):
    """display the history of calls of a particular function"""
    key = method.__qualname__
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {len(inputs)} times:")

    for inp, outp in zip(inputs, outputs):
        print(f"{key}(*{eval(inp)}) -> {outp.decode('utf-8')}")


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    key_input = f"{method.__qualname__}:inputs"
    key_output = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(key_input, str(args))
        result = method(self, *args)
        self._redis.rpush(key_output, result)
        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """define the decorator that increments the count
    for that key every time the method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap the decorated function and return the wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """declares a Cache redis class"""

    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        rand_num = str(uuid.uuid4())
        self._redis.set(rand_num, data)
        return rand_num

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """return value as a string"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """return value as a intger"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
