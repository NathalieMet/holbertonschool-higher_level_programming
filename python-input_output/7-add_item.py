#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file
import sys
from os.path import isfile

def load_add_save():
    """function that creates an Object from a “JSON file”"""
    try:
        var = load_from_json_file("add_item.json")
    except FileNotFoundError:
        var = []

    arg = sys.argv[1:]
    if arg:
        var.extend(arg)

    save_to_json_file(var, "add_item.json")
