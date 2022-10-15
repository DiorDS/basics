#import tomllib #for python 3.11
import pathlib

import tomli as tomllib

wp = pathlib.Path(__file__).parent

with open(wp / "base_config.toml", mode="rb") as fp:
     config = tomllib.load(fp)

assert config == {"PY-ENV":{"secret_key": "36ed6ds67d#@$%6d7s6d//^RD&^%6%&*rfdsdsytf"}}