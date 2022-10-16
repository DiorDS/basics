import time
import requests
from typing import Callable




def safe(func: Callable) -> Callable:
    def _wrapper(*args, **kwargs):
        try:
            start = time.perf_counter_ns()
            result = func(*args, **kwargs)
            return (result, (time.perf_counter_ns() - start) / 10000000)
        
        except Exception as e:
            return (None, e)

    return _wrapper


@safe
def call():
    requests.get("https://ya.ru")


print(call())
print(call())