from collections import defaultdict
from typing import List


def sudoku_validator(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == "0":
                continue
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

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
