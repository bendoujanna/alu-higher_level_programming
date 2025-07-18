#!/usr/bin/python3
"""That module returns a list a int representing the
Pascal's triangle of n"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with 1

        for j in range(1, len(prev_row)):
            # Add the sum of two elements from the previous row
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
