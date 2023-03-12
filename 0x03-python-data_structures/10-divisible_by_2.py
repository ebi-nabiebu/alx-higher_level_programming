#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Function finds all multiples of 2 in a list."""
    multipleof = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            multipleof[i] = 1
        else:
            multipleof[i] = 0

    return multipleof
