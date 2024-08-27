#!/usr/bin/python3
"""
Function that returns the perimeter of the island described in grid:
"""


def island_perimeter(grid):
    """Method Calculates the perimeter of a single island in a 2D grid.

    Args:
        grid: A 2D list of integers representing the grid.
            - 0 represents water
            - 1 represents land

    Returns:
        The perimeter of the island.
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                neighbors = 0
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    neighbors += 1
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors += 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    neighbors += 1
                perimeter += 4 - neighbors

    return perimeter
