import tempfile
from typing import List


def get_temp_directory() -> str:
    """Return a path to a temp directory. Minimal shim for testing."""
    return tempfile.gettempdir()


def get_filename_list(key: str) -> List[str]:
    """Return a list of filenames for known keys. Minimal shim: return empty list."""
    # Known keys in this project: "checkpoints"
    return []
