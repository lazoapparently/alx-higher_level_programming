#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
  """Check if an object is exactly as an instance given class.
    Args:
        Obj (any): The object to check.
        a_class (type): The class to match te type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
