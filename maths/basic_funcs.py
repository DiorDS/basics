from typing import Iterable

__version__ = "v1.0.141022"
__release_tag__ = "Beta for github"

def avg(_list: Iterable[int | float]) -> float | int:
    # Срнеднее арифметическое из списка
    return sum(_list) / len(_list)