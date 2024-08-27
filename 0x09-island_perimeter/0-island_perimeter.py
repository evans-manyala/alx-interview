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
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                neighbors = 0
                if row > 0 and grid[row - 1][col] == 1:
                    neighbors += 1
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    neighbors += 1
                if col > 0 and grid[row][col - 1] == 1:
                    neighbors += 1
                if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                    neighbors += 1
                perimeter += 4 - neighbors

    return perimeter
