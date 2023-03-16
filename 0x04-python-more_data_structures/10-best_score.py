#!/usr/bin/python3

def best_score(eb_dictionary):
    """Function returns a key with the biggest integer value."""
    if eb_dictionary and len(eb_dictionary):
        biggest = list(eb_dictionary.keys())[0]
        for key in eb_dictionary:
            if eb_dictionary[key] > eb_dictionary[biggest]:
                biggest = key
        return biggest
    return None
