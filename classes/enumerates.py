from enum import Enum


class Colors(Enum):
    RED = 1
    BLUE= 2
    GEEEN = 3
    MAGENTA = 4
    PURPLE = 5
    GOLD = 6


main_color = Colors.MAGENTA

if main_color == (Colors.GOLD or Colors.RED):
    print("Привет от баскова")

else:
    print(main_color)