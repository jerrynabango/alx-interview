#!/usr/bin/python3
"""
Challenge of placing N non-attacking queens on an N×N chessboard.
Program that solves the N queens problem.
"""

import sys

def solve_queens(temp, solutions, used_columns, current_row, board_size):
    """Function that solves_n_queens"""
    if current_row > board_size:
        solutions.append(temp[:])
        return solutions

    for column in range(board_size + 1):
        if current_row == 0 or (current_row - 1, column - 1) not in temp and \
                                (current_row - 1, column + 1) not in temp and \
                                column not in used_columns:
            if current_row > 1:
                is_diagonal = False
                for k in range(2, current_row + 1):
                    if (current_row - k, column - k) in temp or \
                       (current_row - k, column + k) in temp:
                        is_diagonal = True
                        break
                if is_diagonal:
                    continue
            
            temp.append((current_row, column))
            used_columns.append(column)
            solve_queens(temp, solutions, used_columns, current_row + 1, board_size)
            used_columns.pop()
            temp.pop()

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if not isinstance(board_size, int):
        print("N must be a number")
        exit(1)
    elif board_size < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_queens([], [], [], 0, board_size - 1)
    for solution in solutions:
        print(solution)
