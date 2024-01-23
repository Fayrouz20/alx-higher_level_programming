#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for item in range(len(matrix)):
            for row in range(len(matrix[item])):
                if row != len(matrix[item]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[item][row]),end=endspace)
            print()
