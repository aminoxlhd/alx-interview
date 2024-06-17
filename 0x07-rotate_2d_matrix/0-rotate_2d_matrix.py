#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(input_matrix):
    """Rotates a 2D matrix in-place by 90 degrees clockwise.

        Args:
            matrix: A list of lists representing the 2D matrix.

        Returns:
            None. The matrix is rotated in-place.
        """
    num_rows = len(input_matrix)
    for start_row in range(num_rows // 2):
        for col_index in range(start_row, num_rows - start_row - 1):
            temp_value = input_matrix[start_row][col_index]
            input_matrix[start_row][col_index] = input_matrix[
                num_rows - 1 - col_index][start_row]
            input_matrix[num_rows - 1 - col_index][start_row] = input_matrix[
                num_rows - 1 - start_row][
                num_rows - 1 - col_index]
            input_matrix[num_rows - 1 - start_row][
                num_rows - 1 - col_index] = input_matrix[col_index][
                num_rows - 1 - start_row]
            input_matrix[col_index][num_rows - 1 - start_row] = temp_value
