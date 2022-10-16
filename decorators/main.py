import time
from typing import Callable

from requests import get


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
    result = get("https://ya.ru")
    print(result.status_code)
    print(result.text[:30])


for _ in range(5):
    print(call())