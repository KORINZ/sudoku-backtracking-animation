from collections import defaultdict
from typing import List


def sudoku_validator(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == "0":
                continue

            # Check row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check Column
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check box
            if val in squares[(r // 3, c // 3)]:
                return False
            squares[(r // 3, c // 3)].add(val)

    return True


if __name__ == '__main__':
    # An edge case that sudoku_validator.py cannot correctly validate the sudoku board
    # However, backtrack function inside sudoku_solver.py will return false
    INPUT_BOARD = [['9', '2', '3', '4', '7', '8', '5', '6', '0'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '8'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '7'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '6'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '5'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '4'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '3'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '2'],
                   ['0', '0', '0', '0', '0', '0', '0', '0', '1']]

    print(sudoku_validator(INPUT_BOARD))  # Incorrect output
