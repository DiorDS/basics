import time
from typing import Any, Callable

from requests import get


def safe(func: Callable) -> Callable:
    def _wrapper(*args, **kwargs) -> tuple[Any, dict]:
        try:
            start = time.perf_counter_ns()
            result = func(*args, **kwargs)
            report = {
                "time": (time.perf_counter_ns() - start) / 10000000,
                "sucsess": True,
                "error": None
            }
            return (result, report)
        
        except Exception as e:
            report = {
                "time": (time.perf_counter_ns() - start) / 10000000,
                "sucsess": False,
                "error": str(e)
            }
            return (None, report)

    return _wrapper


@safe
def call():
    result = get("https://ya.ru")
    print(result.status_code)


for _ in range(5):
    print(call())