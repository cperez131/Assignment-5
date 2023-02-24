from a5 import Board
from typing import *

# CODE TO PLAY SUDOKU YOURSELF
# the code below lets you play sudoku yourself, can't let the computers have all the fun
# 😃 uncomment the lines at the very bottom of the file to play!


def is_valid(board: Board, row_input: int, col_input: int, val_input: int) -> bool:
    """Checks to see if the move you're trying to make is valid

    Args:
        board - board to place move on
        row_input - row coordinate
        col_input - column coordinate
        val_input - value to place

    Returns:
        True if valid, False else
    """

    # check for subgrid
    for i, j in board.subgrid_coordinates(row_input, col_input):
        if val_input == board.rows[i][j]:
            return False

    # check for row
    row_attempting = board.rows[row_input]
    if val_input in row_attempting:
        return False

    # column getter
    # loop through rows and add columns
    col_lists = [r[col_input] for r in board.rows]
    if val_input in col_lists:
        return False

    return True


def play_sudoku(b: Board) -> None:
    """Uses your class to play TicTacToe"""

    def star_surround(val: Any) -> str:
        return f"\n************ {val} ************\n"

    while not b.goal_test() or b.failure_test():
        b.print_pretty()

        # validate inputs individually
        val_in = int(input(f"What number (1-9) would you like to place?  "))
        if val_in < 1 or val_in > 9:
            print(star_surround("Invalid value. Try again."))
            continue

        row_in = int(input(f"Enter row (0-8) to place {val_in} in:  "))
        if row_in < 0 or row_in > 8:
            print(star_surround("Invalid row. Try again from the start."))
            continue

        col_in = int(input(f"Enter column (0-8) to place {val_in} in:  "))
        if col_in < 0 or col_in > 8:
            print(star_surround("Invalid column. Try again from the start."))
            continue

        print(f"Placing {val_in} at ({row_in}, {col_in}).  \n")

        valid = is_valid(b, row_in, col_in, val_in)
        if valid:
            b.update(row_in, col_in, val_in)
        else:
            print(
                star_surround("Invalid move - already in row/col/subgrid - TRY AGAIN")
            )

    if b.goal_test():
        print("WOO YOU COMPLETED THE GAME!")

    if b.failure_test():
        print("There's been a problem. This board won't work")


first_moves = [
    (0, 1, 7),
    (0, 7, 1),
    (1, 2, 9),
    (1, 3, 7),
    (1, 5, 4),
    (1, 6, 2),
    (2, 2, 8),
    (2, 3, 9),
    (2, 6, 3),
    (3, 1, 4),
    (3, 2, 3),
    (3, 4, 6),
    (4, 1, 9),
    (4, 3, 1),
    (4, 5, 8),
    (4, 7, 7),
    (5, 4, 2),
    (5, 6, 1),
    (5, 7, 5),
    (6, 2, 4),
    (6, 5, 5),
    (6, 6, 7),
    (7, 2, 7),
    (7, 3, 4),
    (7, 5, 1),
    (7, 6, 9),
    (8, 1, 3),
    (8, 7, 8),
]

second_moves = [
    (0, 1, 2),
    (0, 3, 3),
    (0, 5, 5),
    (0, 7, 4),
    (1, 6, 9),
    (2, 1, 7),
    (2, 4, 4),
    (2, 7, 8),
    (3, 0, 1),
    (3, 2, 7),
    (3, 5, 9),
    (3, 8, 2),
    (4, 1, 9),
    (4, 4, 3),
    (4, 7, 6),
    (5, 0, 6),
    (5, 3, 7),
    (5, 6, 5),
    (5, 8, 8),
    (6, 1, 1),
    (6, 4, 9),
    (6, 7, 2),
    (7, 2, 6),
    (8, 1, 4),
    (8, 3, 8),
    (8, 5, 7),
    (8, 7, 5),
]

b = Board()
# change first_moves to second_moves to play that game instead
for move in first_moves:
    b.update(*move)
play_sudoku(b)
