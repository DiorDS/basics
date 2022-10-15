from enum import Enum
from classes.enumerates import Colors
from maths.basic_funcs import avg


assert issubclass(Colors, Enum)
assert avg([1,2,3,4]) == 2.5
