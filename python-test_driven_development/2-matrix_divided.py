#!/usr/bin/python3
"""
This module contains a function to divide all elements of a matrix by a number.
It checks for valid matrix structure, row sizes, element types,
 and div validity.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Parameters:
        matrix (list of lists of int/float): matrix to divide
        div (int or float): number to divide by

    Returns:
        list of lists of floats: new matrix with divided elements

    Raises:
        TypeError: if matrix elements are invalid or rows have different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or not matrix or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if row_length == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row] for row in matrix
    ]

    return new_matrix
