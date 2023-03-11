from collections import defaultdict
from typing import List, Tuple
from copy import deepcopy

STRING_NUMBERS = [str(n) for n in range(1, 10)]


def print_board(board: List[List[str]]) -> None:
    board_copy = deepcopy(board)
    print("-" * 25)
    for i, row in enumerate(board_copy):
        for j, num in enumerate(row):
            if num == "0":
                row[j] = "."
        row_str = " | ".join([" ".join(map(str, row[m:m + 3]))
                              for m in range(0, len(row), 3)])
        print(f'| {row_str} |')
        if (i + 1) % 3 == 0:
            print("-" * 25)


def sudoku_solver(input_board: List[List[str]]) -> List[List[str]]:
    board = deepcopy(input_board)
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    # Place existing numbers to the gird
    for row in range(9):
        for col in range(9):
            if board[row][col] != "0":
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])

    # Check if a number can be placed according to the constraints
    def can_place_number(r: int, c: int, num: str) -> bool:
        if (num in rows[r]) or (num in cols[c]) or (num in boxes[(r // 3, c // 3)]):
            return False
        else:
            return True

    def place_number_in_cell(r: int, c: int, num: str) -> None:
        board[r][c] = num
        rows[r].add(num)
        cols[c].add(num)
        boxes[(r // 3, c // 3)].add(num)

    def remove_number_in_cell(r: int, c: int, num: str) -> None:
        board[r][c] = "0"
        rows[r].remove(num)
        cols[c].remove(num)
        boxes[(r // 3, c // 3)].remove(num)

    def move_to_next_cell(r: int, c: int) -> Tuple[int, int]:
        # Move to next column
        if c < 8:
            new_r, new_c = r, c + 1
        # Move to next row, reset column index
        else:
            new_r, new_c = r + 1, 0
        return new_r, new_c

    def backtrack(r: int, c: int) -> bool:
        # Base case: reached last row + 1
        if r > 8:
            return True

        # If a number already existed in the cell, move to the next cell
        if board[r][c] != "0":
            new_r, new_c = move_to_next_cell(r, c)
            return backtrack(new_r, new_c)

        # If a number can be placed, place it to the board
        for num in STRING_NUMBERS:
            if can_place_number(r, c, num):
                place_number_in_cell(r, c, num)
                if backtrack(r, c):
                    return True
                else:
                    remove_number_in_cell(r, c, num)

        # The sudoku is not solvable
        return False

    backtrack(0, 0)

    # Return the original input board if the sudoku board is not valid
    if board != input_board:
        return board
    else:
        return input_board


if __name__ == '__main__':
    INPUT_BOARD = [['5', '3', '0', '0', '7', '0', '0', '0', '0'],
                   ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
                   ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
                   ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
                   ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
                   ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
                   ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
                   ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
                   ['0', '0', '0', '0', '8', '0', '0', '7', '9']]
    print('\nGiven:')
    print_board(INPUT_BOARD)

    # Solve the Sudoku board
    solution = sudoku_solver(INPUT_BOARD)

    if solution != INPUT_BOARD:
        print('\nSolution:')
        print_board(solution)
    else:
        print('\nNot a valid Sudoku board.')
