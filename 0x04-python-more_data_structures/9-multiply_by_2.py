#!/usr/bin/python3

def multiply_by_2(eb_dictionary):
    """Function returns a new dictionary with all values multiplied by 2."""
    return {key: value * 2 for key, value in eb_dictionary.items()}
