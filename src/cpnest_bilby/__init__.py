"""Plugin for bilby to use the CPNest nested sampling algorithm."""

from importlib.metadata import PackageNotFoundError, version

from .plugin import CPNest

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

__all__ = ["CPNest"]
