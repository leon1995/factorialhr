import os

try:
    __version__ = os.environ["FACTORIALHR_VERSION"]
except KeyError:
    from importlib import metadata

    try:
        __version__ = metadata.version("factorialhr")
    except metadata.PackageNotFoundError:
        __version__ = "0.0.0"
