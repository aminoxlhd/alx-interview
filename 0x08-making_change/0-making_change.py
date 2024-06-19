#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    index = 0
    current_sum = 0
    changes = 0
    while index < len(coins) and current_sum < total:
        while coins[index] <= (total - current_sum):
            current_sum = current_sum + coins[index]
            changes = changes + 1
            if current_sum == total:
                return changes
        index = index + 1
    return -1
