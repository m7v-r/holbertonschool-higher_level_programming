#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module provides one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be a non-zero integer or float.

    Returns:
        A new matrix containing the divided elements.

    Raises:
        TypeError: If the matrix is invalid, rows are uneven,
            or div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for NaN specifically (NaN is never equal to itself)
    if div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = None

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
            if element != element:
                raise TypeError(msg)

    return [[round(item / div, 2) for item in row] for row in matrix]
