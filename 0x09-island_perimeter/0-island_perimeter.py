#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    # Initialize the perimeter
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is land
            if grid[i][j] == 1:
                # Check all four possible directions (up, down, left, right)
                # and add to the perimeter if the neighboring
                # cell is water or out of bounds
                # Check upwards
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check downwards
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
