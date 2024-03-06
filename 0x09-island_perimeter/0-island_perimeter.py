#!/usr/bin/python3
"""
     This is the Island perimeter computing module
"""


def island_perimeter(grid):
    """
      This computes the perimeter of an island with no lakes
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    a = len(grid)
    for b, row in enumerate(grid):
        c = len(row)
        for d, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                b == 0 or (len(grid[b - 1]) > d and grid[b - 1][d] == 0),
                d == c - 1 or (c > d + 1 and row[d + 1] == 0),
                b == a - 1 or (len(grid[b + 1]) > d and grid[b + 1][d] == 0),
                d == 0 or row[d - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
