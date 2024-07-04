#!/usr/bin/python3
""" Prime Game  """


def findPrimes(n):
    """
    This function finds all prime numbers between 1 and n
    """
    primes = []
    if n >= 2:
        primes.append(2)
    for num in range(3, n + 1, 2):
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """
    determine who the winner of a game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    countA = 0
    countB = 0
    for n in range(x):
        primes = findPrimes(nums[n])
        if len(primes) % 2 != 0:
            countA = countA + 1
        else:
            countB = countB + 1
    if countA == countB:
        return None
    if countA > countB:
        return "Maria"
    else:
        return "Ben"
