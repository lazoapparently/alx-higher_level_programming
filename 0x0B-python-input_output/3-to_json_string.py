#!/usr/bin/python3
'''A module containing IO functions.
'''
from json import JSONEncoder


def to_json_string(my_obj):
    """Creates the JSON representation of an object.
    Args:
        my_obj: An object to convert to JSONte to.
    Returns:
        str: A JSON rep of object.
    """
    return JSONEcoder().encode(my_obj)
