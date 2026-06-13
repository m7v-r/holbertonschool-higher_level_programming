#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
The module provides one function, lazy_matrix_mul(m_a, m_b).
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a: The first matrix (list of lists of ints/floats).
        m_b: The second matrix (list of lists of ints/floats).

    Returns:
        The matrix product as a NumPy array.
    """
    return np.matmul(m_a, m_b)
