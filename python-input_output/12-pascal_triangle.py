#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []
    triangle = []
    for index in range(n):
        row = []
        row.append(1)
        if index > 0:
            prev_row = triangle[index - 1]
            for jindex in range(1, len(prev_row)):
                row.append(prev_row[jindex - 1] + prev_row[jindex])
            row.append(1)
        triangle.append(row)
    return triangle
