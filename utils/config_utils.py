"""
JSON configuration and data file utilities.
Only load/save - no magic.
"""
import json
import os


def load_json(filepath: str) -> dict:
    """Load JSON file and return dict"""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(filepath: str, data: dict) -> None:
    """Save dict to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def get_project_root() -> str:
    """Get project root directory (two levels up from this file)"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_file_path(filename: str = "test_data.json") -> str:
    """Get absolute path to data file"""
    return os.path.join(get_project_root(), "data", filename)