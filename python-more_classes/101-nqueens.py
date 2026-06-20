#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for r, c in board:
        if c == col or \
           abs(r - row) == abs(c - col):
            return False
    return True

def solve_nqueens(n, row, current_board, solutions):
    """Backtracking algorithm to find all solutions."""
    if row == n:
        solutions.append(list(current_board))
        return

    for col in range(n):
        if is_safe(current_board, row, col):
            current_board.append([row, col])
            solve_nqueens(n, row + 1, current_board, solutions)
            current_board.pop()

if __name__ == "__main__":
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

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for sol in solutions:
        print(sol)
