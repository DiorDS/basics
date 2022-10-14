import tomllib

with open("base_config.toml", mode="rb") as fp:
     config = tomllib.load(fp)

print(config)