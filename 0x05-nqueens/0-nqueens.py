#!/usr/bin/python3
"""N queens"""
import sys


def is_safe(row, col, queens):
    """
          A fnction that check in the place is safe.

          Args:
              row: The row to place the queen.
              col: The column to place the queen.
              queens: A list of existing queen positions (tuples of row, col).

          Returns:
              True if the position is safe, False otherwise.
          """
    for r, c in queens:
        if r == row or c == col:
            return False

    n = len(queens)
    for i in range(n):
        r, c = queens[i]
        if abs(row - r) == abs(col - c):
            return False

    return True


def solve_n_queens(n, queens):
    """
    A function that solves the N-Queens problem using backtracking.

    Args:
        n: The number of queens.
        queens: A list of existing queen positions (tuples of row, col).

    Returns:
        None
    """


if len(queens) == n:
    print(queens)
    return

for col in range(n):
    if is_safe(len(queens), col, queens):
        queens.append((len(queens), col))
        solve_n_queens(n, queens)
        queens.pop()


def main():
    """
    The Main Function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n, [])


if __name__ == "__main__":
    main()
