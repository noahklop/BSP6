import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# get path of pyproject.toml file
path = pathlib.Path(__file__).parent.parent / "pyproject.toml"
with path.open(mode="rb") as fp:
    project = tomllib.load(fp)

class MissingParameter(Exception):
    """ Custom exception for missing parameter """
    def __init__(self, parameter, additional_info) -> None:
        self.message = f"The parameter {parameter} has not been set correctly. {additional_info}"
        super().__init__(self.message)