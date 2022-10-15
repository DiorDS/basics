#import tomllib #for python 3.11
import pathlib

import tomli as tomllib

wp = pathlib.Path(__file__).parent

with open(wp / "base_config.toml", mode="rb") as fp:
     config = tomllib.load(fp)

