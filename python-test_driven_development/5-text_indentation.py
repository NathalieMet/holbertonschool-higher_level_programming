#!/usr/bin/python3
"""
This function prints a text with 2 new lines after each of these characters:
 ., ? and :

"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n').replace('?', '?\n\n') \
                                     .replace(':', ':\n\n')
    paragraphs = text.split('\n')
    for i, paragraph in enumerate(paragraphs):
        if i == len(paragraphs) - 1:
            print(paragraph.strip(), end='')
        else:
            print(paragraph.strip())
