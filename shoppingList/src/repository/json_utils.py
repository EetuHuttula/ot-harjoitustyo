"""Utility functions for JSON file operations."""
import json


def load_raw(data_file):
    """Load raw JSON list from file.

    Args:
        data_file: Path object to the JSON file.

    Returns:
        List of records or empty list if file cannot be read.
    """
    try:
        with data_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        data = []

    if not isinstance(data, list):
        data = []
    return data


def save_raw(data_file, records):
    """Save raw JSON list to file.

    Args:
        data_file: Path object to the JSON file.
        records: List of records to save.
    """
    with data_file.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
