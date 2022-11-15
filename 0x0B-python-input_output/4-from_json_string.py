#!/usr/bin/python3
"""A module containing IO functions.
"""
from json import JSONDecoder


def to_json_string(my_str):
    """Creates the JSON representation of an object.
    Args:
        my_obj: An object to convert to JSONte to.
    Returns:
        str: A JSON rep of object.
        otherwise an eception is thrown
    """
    return JSONDecoder().decode(my_str)
