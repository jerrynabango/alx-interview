#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """2D matrix, rotate it 90 degrees clockwise."""
    rotate = 0
    for clockwise in list(zip(*matrix)):
        matrix[rotate][:] = clockwise[::-1]
        rotate += 1
