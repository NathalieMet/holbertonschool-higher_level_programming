#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 123:
            uppercase_char = (chr(ord(char) - 32))
        else:
            uppercase_char = char
        print(uppercase_char, end='')
    print('\n', end='')
