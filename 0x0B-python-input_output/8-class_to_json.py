#!/usr/bin/python3
"""
A module containing IO functions.
"""


def class_to_json(obj):
    """
    Retrieves dictionary desc. of object
    Args:
        obj (any): An obj whose attri are to be retrieved.
    Returns:
        DICT: tHE ATTR of the obj otherwise none.
    """
    if '__dict__' in dir(obj):
        return obj.__dict__
