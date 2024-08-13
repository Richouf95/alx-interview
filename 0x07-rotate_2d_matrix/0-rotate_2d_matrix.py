#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Test 0x07 - Rotate 2D Matrix
    """

    n = len(matrix)

    # Transposer la matrice
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Inverser chaque ligne
    for i in range(n):
        matrix[i].reverse()
