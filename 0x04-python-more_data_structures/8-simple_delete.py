#!/usr/bin/python3

def simple_delete(eb_dictionary, key=""):
    """Function deletes a key in a dictionary."""
    if key in eb_dictionary:
        del eb_dictionary[key]
    return eb_dictionary
