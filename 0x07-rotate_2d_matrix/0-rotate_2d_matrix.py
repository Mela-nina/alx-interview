#!/usr/bin/python3
"""
This is the Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    This givens an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for s in range(first, last):
            top = matrix[first][s]
            matrix[first][s] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[s][last]
            matrix[s][last] = top
            offset += 1
