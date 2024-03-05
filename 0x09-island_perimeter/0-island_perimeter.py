#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid:
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    """
    width = len(grid)
    height = len(grid[0])
    perimeter = 0
    for w in range(width):
        for h in range(height):
            if grid[w][h] == 1:
                perimeter += 4
                if h < height - 1 and grid[w][h + 1] == 1:
                    perimeter -= 2
                if w < width - 1 and grid[w + 1][h] == 1:
                    perimeter -= 2
    return perimeter
