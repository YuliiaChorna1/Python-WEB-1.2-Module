# "RIGHT WAY" Decorators

import time
from functools import wraps

def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"func {func.__name__}: {end - start}")
        return result
    return wrapper

def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"func {func.__name__}: {end - start}")
        return result
    return wrapper

@wrong_timelogger
def long_loop(num):
    """
    Long loop function
    
    :param num:
    :return: None
    """
    while num > 0:
        num -= 1

if __name__ == '__main__':
    long_loop(100000)
    print(long_loop.__name__) # wrapper
    print(long_loop.__doc__) # None
    print(long_loop.__annotations__) # {}