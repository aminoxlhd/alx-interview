#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file
    Args:
        n: The number of characters.
    Returns:
        The minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return n

    current_string = 'H'
    num_operations = 0
    while len(current_string) < n:
        if n % len(current_string) == 0:
            num_operations = num_operations + 2
            current_string += current_string
        else:
            if len(current_string) * 2 <= n:
                num_operations = num_operations + 2
                current_string += current_string
            else:
                copy_length = min(n - len(current_string), len(current_string))
                num_operations = num_operations + 1
                current_string += current_string[:copy_length]

    if len(current_string) + 1 == n:
        num_operations = num_operations + 1
        current_string += current_char

    return num_operations
