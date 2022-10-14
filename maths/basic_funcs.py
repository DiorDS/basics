from typing import Iterable


def avg(_list: Iterable[int | float]) -> float | int:
    return sum(_list) / len(_list)