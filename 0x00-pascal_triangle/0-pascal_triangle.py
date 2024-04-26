#!/usr/bin/python
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle function"""
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
