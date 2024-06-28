#!/usr/bin/python3
"""
sland Perimeter
"""


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
    number_of_rows = len(grid)
    for row_index, row in enumerate(grid):
        number_of_cells = len(row)
        for cell_index, cell_value in enumerate(row):
            if cell_value != 0:
                is_border = (
                    row_index == 0 or (len(
                        grid[row_index - 1]) > cell_index and grid[
                        row_index - 1][cell_index] == 0),
                    cell_index == number_of_cells - 1 or (
                            number_of_cells > cell_index + 1 and row[
                                cell_index + 1] == 0),
                    row_index == number_of_rows - 1 or (len(
                        grid[row_index + 1]) > cell_index and grid[
                        row_index + 1][cell_index] == 0),
                    cell_index == 0 or row[cell_index - 1] == 0,
                )
                perimeter += sum(is_border)

    return perimeter
