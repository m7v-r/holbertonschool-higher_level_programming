#!/usr/bin/python3
"""
This module contains a function that generates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        # Calculate intermediate values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
