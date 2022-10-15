from enum import Enum
from classes.enumerates import Colors
from maths.basic_funcs import avg
from toml_test.toml_example import config


assert issubclass(Colors, Enum)
assert avg([1,2,3,4]) == 2.5
assert config == {"PY-ENV":{"secret_key": "36ed6ds67d#@$%6d7s6d//^RD&^%6%&*rfdsdsytf"}}


print("All tests gets good results!")