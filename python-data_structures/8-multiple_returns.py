#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first_letter = (None)
    else:
        first_letter = (sentence[0])
    return (length, first_letter)
