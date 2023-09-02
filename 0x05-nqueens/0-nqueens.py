#!/usr/bin/python3
"""
    N-queen problem
    The next algo solve any N queen in any NxN
    Being N > 3
"""
import sys


def is_valid_move(board, row, col, n):
    """
    Returns True if it's possible to place a queen at position (row, col)
    on the board with size n, otherwise False.
    """
    # Check row and column
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check diagonals
    for i in range(n):
        for j in range(n):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True


def solve_n_queens(n):
    """
    Returns a list of all possible solutions to the N Queens problem
    with board size n.
    """
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []

    def solve(row, solution):
        if row == n:
            # Found a solution, add it to the list of solutions
            solutions.append(solution[:])
            return

        for col in range(n):
            if is_valid_move(board, row, col, n):
                # Place the queen at position (row, col)
                board[row][col] = 1
                solution.append([row, col])

                # Recursively solve the subproblem with the next row
                solve(row + 1, solution)

                # Remove the queen at position (row, col)
                board[row][col] = 0
                solution.pop()

    # Start solving the problem with the first row
    solve(0, [])

    # Convert solutions to the desired output format
    formatted_solutions = []
    for solution in solutions:
        formatted_solution = []
        for row, col in solution:
            formatted_solution.append([row, col])
        formatted_solutions.append(formatted_solution)

    return formatted_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    for soln in solve_n_queens(n):
        print(soln)
