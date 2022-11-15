#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads the file

    Args:
        Filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
