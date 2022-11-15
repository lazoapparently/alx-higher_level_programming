#!/usr/bin/python3
"""A module containing IO functions.
"""
from json import JSONEncoder


def save_to_json_file(my_obj, filename):
    """Saves the JSON representation of an object.
    Args:
        my_obj: An object to convert to JSONte to.
        filename (str): The file to save the JSON string in.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(JSONEncoder().encode(my_obj))
