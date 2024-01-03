#!/usr/bin/python3
"""
	This is  the Pascal's Triangle function
"""


def pascal_triangle(n):
    """ This returns a list of lists of integers representing
        the Pascal's triangle of n
    """
    triangle = []
    for s in range(1, n+1):
        row = []
        for t in range(s):
            if t == 0 or t == s-1:
                n = 1
                row.append(r)
            else:
                n = triangle[s-2][t-1] + triangle[s-2][t]
                row.append(n)
        triangle.append(row)

    return triangle
