from typing import Iterable


def avg(_list: Iterable[int | float]) -> float | int:
    # Срнеднее арифметическое из списка
    return sum(_list) / len(_list)