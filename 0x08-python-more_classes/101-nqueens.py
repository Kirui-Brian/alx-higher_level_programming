#!/usr/bin/python3
"""
N Queens puzzle solver
"""

import sys


def print_usage_and_exit():
    """
    Prints the usage message and exits with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """
    Prints the number error message and exits with status 1.
    """
    print("N must be a number")
    sys.exit(1)


def print_size_error_and_exit():
    """
    Prints the size error message and exits with status 1.
    """
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board at (row, col).
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """
    Utilizes backtracking to find all solutions.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0
    return res


def solve_nqueens(n):
    """
    Solves the N Queens puzzle and returns all solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()
    if n < 4:
        print_size_error_and_exit()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
