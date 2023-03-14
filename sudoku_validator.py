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
    INPUT_BOARD = [['5', '3', '0', '0', '7', '0', '0', '0', '0'],
                   ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
                   ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
                   ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
                   ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
                   ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
                   ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
                   ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
                   ['0', '0', '0', '0', '8', '0', '0', '7', '9']]

    print(Validator().sudoku_validator(INPUT_BOARD))
