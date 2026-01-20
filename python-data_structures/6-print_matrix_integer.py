#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, integer in enumerate(row):
            if index != len(row) - 1:
                print("{}".format(integer), end=" ")
            else:
                print("{}".format(integer), end="")
        print()
