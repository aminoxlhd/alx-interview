#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in-place by 90 degrees clockwise.

        Args:
            matrix: A list of lists representing the 2D matrix.

        Returns:
            None. The matrix is rotated in-place.
        """
    num_rows = len(matrix)

    for layer in range(num_rows // 2):
        first_index = layer
        last_index = num_rows - 1 - layer
        for i in range(first_index, last_index):
            temp = matrix[first_index][i]
            matrix[first_index][i] = matrix[last_index - i][first_index]
            matrix[last_index - i][first_index] = matrix[last_index][
                last_index - i]
            matrix[last_index][last_index - i] = matrix[i][last_index]
            matrix[i][last_index] = temp
