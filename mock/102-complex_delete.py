#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, val in a_dictionary.items():
        if val == value:
            var_key = [key]
    for elemn in var_key:
        del a_dictionary[var_key]
    return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
print(a_dictionary)
print("--")
new_dict = complex_delete(a_dictionary, 'C')
print(new_dict)
