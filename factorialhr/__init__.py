import os

try:
    __version__ = os.environ['FACTORIALHR_VERSION']
except KeyError:
    from importlib import metadata

    __version__ = metadata.version('factorialhr')
