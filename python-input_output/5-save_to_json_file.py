#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON
representation:"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON
    representation:"""
    with open(filename, 'w') as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
