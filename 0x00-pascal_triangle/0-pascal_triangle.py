#!/usr/bin/python3
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
        index2 = 1
        while index2 <= index:
            if index == 0:
                prev_row = [1]
            else:
                prev_row = triangle[index - 1]

                if index2 < index:
                    element = prev_row[index2 - 1] + prev_row[index2]
                else:
                    element = prev_row[index2 - 1]

                row.append(element)
                index2 += 1

        triangle.append(row)

    return triangle
