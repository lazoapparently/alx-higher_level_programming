#!/usr/bin/python3
"""A module containing IO functions.
"""
from json import JSONEncoder


def load_from_json_file(filename):
    """Creates an object the JSON representation of an object.
    Args:
        filename (str): The file to save the JSON string in.
    Returns:
        any: An object corresponding JSON String
        otherwise an exception is thrown.
    """
    lines = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    return JSONDecoder().decode(''.join(lines))
