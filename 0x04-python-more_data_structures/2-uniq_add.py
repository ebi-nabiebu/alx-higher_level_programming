#!/usr/bin/python3

def uniq_add(my_list=[]):
    add_unq = 0
    for eb in set(my_list):
        add_unq += eb
    return add_unq
