#!/usr/bin/python3
""" This is the Pascal Triangle Interview Function"""


def pascal_triangle(r):
    """This returns a list of lists of numbers
    representing the Pascal's triangle of r"""
    if r <= 0:
        return []

    triangle = [[1]]

    for s in range(1, r):
        row = [1]

        for t in range(1, s):
            row.append(triangle[s-1][t-1] + triangle[s-1][t])
        row.append(1)
        triangle.append(row)

    return triangle
