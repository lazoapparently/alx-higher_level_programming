#!/usr/bin/python3
"""
    A script adds all argus to a Python list, save to a file
"""
import sys
import os
from importlib import import_module as using


save_to_json_file, load_from_json_file = (
    using('5-save_to_json_file').save_to_json_file,
    using('6-load_from_json_file').load_from_json_file
)
args_list = []
args_list_file_name = 'add_item.json'
"""
    file name of the file containing list of arguments.
"""


def run():
    """
    Runs script routines
    """
    if not os.path.exists(args_list_file_name):
        with open(args_list_file_name, mode='w', encoding='utf-8') as file:
            file.write('[]')
    json_list = load_from_json_file(args_list_file_name)
    if (type(json_list) is list) and all(type(s) is str for s in json_list):
        args_list.extend(json_list)
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, args_list_file_name)


if __name__ == '__main__':
    run()
