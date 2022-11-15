#!/usr/bin/python3
# 0-read_file.py
"""Defines a text file reading function."""


def read_file(filename=""):
    """
    Reads the file

    Args:
        Filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
