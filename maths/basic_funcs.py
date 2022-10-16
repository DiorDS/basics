import math
from typing import Iterable

__version__ = "v1.1.141022"
__release_tag__ = "Beta for github"
__author__ = "IGorunov"
__all__ = ["avg", "median", "std"]

def median(_list: Iterable[int | float])  -> float | int: 
    # Медиана списка
    n = len(_list) 
    mid = n // 2
    if n % 2 == 1:
        return sorted(_list)[mid]
    else:
        return avg(sorted(_list)[mid-1:][:2])

def std(_list: Iterable[int | float])  -> float | int: 
    # Среднеквадратичное списка
    mu = avg(_list)
    n = len(_list) 
    n = n-1 if n in range(1, 30) else n  
    square_deviation = lambda x: (x - mu) ** 2 
    return math.sqrt(sum(map(square_deviation, _list)) / n)

def avg(_list: Iterable[int | float]) -> float | int:
    # Срнеднее арифметическое из списка
    return sum(_list) / len(_list) 