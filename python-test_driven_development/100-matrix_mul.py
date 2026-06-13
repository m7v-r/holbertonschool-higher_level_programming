#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.
The module provides one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a: The first matrix (list of lists of ints/floats).
        m_b: The second matrix (list of lists of ints/floats).

    Returns:
        A new matrix representing the multiplication product.

    Raises:
        TypeError: If matrices are invalid structurally or contain non-numbers.
        ValueError: If matrices are empty or cannot be multiplied.
    """
    # 1. Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Check if m_a or m_b is empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # 4. Check for invalid element types
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Check if rows are of the same size (rectangle)
    a_row_size = len(m_a[0])
    if not all(len(row) == a_row_size for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    b_row_size = len(m_b[0])
    if not all(len(row) == b_row_size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            result_row.append(dot_product)
        result.append(result_row)

    return result
