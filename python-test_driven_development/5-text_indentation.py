#!/usr/bin/python3
"""
This function prints a text with 2 new lines after each of these characters:
 ., ? and :

"""


def text_indentation(text):
    """text_indentation function

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for element in text:
        print(element, end="")
        if element in [".", "?", ":"]:
            print("\n")
