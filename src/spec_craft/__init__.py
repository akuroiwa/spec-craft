from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("spec-craft")
except PackageNotFoundError:
    __version__ = "0.1.7"
