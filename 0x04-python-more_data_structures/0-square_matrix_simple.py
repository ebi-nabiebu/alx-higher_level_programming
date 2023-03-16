#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda eb: eb * eb), elt)) for elt in matrix]
