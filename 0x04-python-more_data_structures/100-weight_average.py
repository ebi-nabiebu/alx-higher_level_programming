#!/usr/bin/python3

def weight_average(my_list=[]):
    """Function that returns the weighted average of all integers tuple."""
    if my_list and len(my_list):
        value = 0
        ebi = 0
        for n_tupl in my_list:
            value += (n_tupl[0] * n_tupl[1])
            ebi += n_tupl[1]

        return (value / ebi)

    return 0
