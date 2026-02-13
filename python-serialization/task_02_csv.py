#!/usr/bin/python3
"""
CSV to JSON converter.

Reads a CSV file and writes its contents as a JSON array of dictionaries
to 'data.json'. Each CSV row becomes a dictionary with headers as keys.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to 'data.json'.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion succeeds, False on error.
    """
    try:
        with open(csv_filename, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            convert = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_f:
            json.dump(convert, json_f, indent=4)
        return True

    except Exception:
        return False
