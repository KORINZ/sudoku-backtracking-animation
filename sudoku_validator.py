from collections import defaultdict
from typing import List


class Validator:
    def __init__(self) -> None:
        self.string_number = [str(n) for n in range(1, 10)]
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.boxes = defaultdict(set)

    def sudoku_validator(self, board: List[List[str]]) -> bool:
        '''Validate a sudoku board.'''

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == "0":
                    continue

                # Check row
                if val in self.rows[r]:
                    return False
                self.rows[r].add(val)

                # Check Column
                if val in self.cols[c]:
                    return False
                self.cols[c].add(val)

                # Check box
                if val in self.boxes[(r // 3, c // 3)]:
                    return False
                self.boxes[(r // 3, c // 3)].add(val)

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

    print(Validator().sudoku_validator(INPUT_BOARD))  # Incorrect output
