#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for items in matrix:
          new_matrix.append([c**2 for c in items])
    return new_matrix
