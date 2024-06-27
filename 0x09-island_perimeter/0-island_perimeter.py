#!/usr/bin/python3
"""sland Perimeter"""

def island_perimeter(grid):
    """
      a function def island_perimeter(grid): that returns the perimeter
      of the island described in grid

      Args:
          grid: a list of integers representing the grid.

      Returns:
          The perimeter of the island described in grid
      """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    perimeter += 1
                    continue

                if grid[row - 1][col] == 0:
                    perimeter += 1
                if grid[row + 1][col] == 0:
                    perimeter += 1
                if col > 0 and grid[row][col - 1] == 0:
                    perimeter += 1
                if col < cols - 1 and grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
