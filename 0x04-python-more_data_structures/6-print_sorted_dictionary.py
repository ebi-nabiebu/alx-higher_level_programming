#!/usr/bin/python3

def print_sorted_dictionary(eb_dictionary):
    """Function prints a dictionary by ordered keys."""
    for key in sorted(eb_dictionary.keys()):
        print("{:s}: {}".format(key, eb_dictionary[key]))
