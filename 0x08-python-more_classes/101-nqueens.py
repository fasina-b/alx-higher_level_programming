#!/usr/bin/python3

"""Solves the N-Queens Puzzle.

Finds all possible solutions for placing N non-attacking queens on chessboard

Example:
    $ ./101-nqueens.py N


N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[row, column], [row, column], [row,
where `row` and `column` represent the position of a queen on the chessboard.
"""
import sys


def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    chessboard = []
    [chessboard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chessboard]
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deep copy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def cross_out(chessboard, row, col):
    """Cross out spots on a chessboard.

    Crosses out spots where non-attacking queens can no
    longer be placed.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Cross out all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Cross out all backward spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Cross out all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Cross out all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Cross out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Cross out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # Cross out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Cross out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-Queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(chessboard):
        solutions.append(get_solution(chessboard))
        return solutions

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_board = deepcopy_chessboard(chessboard)
            tmp_board[row][c] = "Q"
            cross_out(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions
