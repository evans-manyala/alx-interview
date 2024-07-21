#!/usr/bin/env python3
"""
Pascal' Triangle
"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to the nth row.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of lists representing Pascal's
        Triangle, or an empty list if n <= 0.
    """

    if n <= 0:
        return []  # Handle invalid input

    triangle = [[1]]  # Start with the first row (just 1)

    for i in range(1, n):  # Iterate to generate subsequent rows
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Each row starts with 1

        for j in range(1, i):  # Calculate inner numbers
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
