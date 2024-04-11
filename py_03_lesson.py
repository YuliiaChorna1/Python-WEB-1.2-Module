# "RIGHT WAY" Decorators

import time
from functools import wraps


def wrong_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func}: {end - start}")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func}: {end - start}")
        return result
    return wrapper


@logger
def loop(num):
    """DOcumentation"""
    while num > 0:
        num -= 1

loop (100000)
print(loop.__name__)
print(loop.__annotations__)
print(loop.__doc__)