#!/usr/bin/python
"""Triangle Triangle"""

3
def pascal_triangle(n):

    """
    A function that returns a list of lists of integers representing
        the Pascal s triangle of n
    """
    triangle = []

    if n == 0:
        return triangle
    elif n == 1:
        triangle.append([1])
        return triangle

    for index in range(n):
        row = []
        row.append(1)

        if index > 1:
            for index2 in range(1, index):
                prev_row = triangle[index - 1]
                element = prev_row[index2 - 1] + prev_row[index2]
                row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle
