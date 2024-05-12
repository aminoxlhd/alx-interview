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
        return 0

    num_operations = 0
    string_length = 2
    while n > 1:
        while n % string_length == 0:
            n //= string_length
            num_operations = num_operations + string_length
        string_length = string_length + 1

    return num_operations
