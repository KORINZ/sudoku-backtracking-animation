from collections import defaultdict
from typing import List, Tuple
from copy import deepcopy


class Solver:
    def __init__(self) -> None:
        self.string_number = [str(n) for n in range(1, 10)]
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.boxes = defaultdict(set)
        self.board = [["0" for i in range(9)] for i in range(9)]

    def print_board(self, board: List[List[str]]) -> None:
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

    def sudoku_solver(self, input_board: List[List[str]]) -> List[List[str]]:
        self.board = deepcopy(input_board)

        # Place existing numbers to the gird
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != "0":
                    self.rows[row].add(self.board[row][col])
                    self.cols[col].add(self.board[row][col])
                    self.boxes[(row // 3, col // 3)].add(self.board[row][col])

        self.backtrack(0, 0)
        # Return the original input board if the sudoku board is not valid
        if self.board != input_board:
            return self.board
        else:
            return input_board

        # Check if a number can be placed according to the constraints

    def can_place_number(self, r: int, c: int, num: str) -> bool:
        if (num in self.rows[r]) or (num in self.cols[c]) or (num in self.boxes[(r // 3, c // 3)]):
            return False
        else:
            return True

    def place_number_in_cell(self, r: int, c: int, num: str) -> None:
        self.board[r][c] = num
        self.rows[r].add(num)
        self.cols[c].add(num)
        self.boxes[(r // 3, c // 3)].add(num)

    def remove_number_in_cell(self, r: int, c: int, num: str) -> None:
        self.board[r][c] = "0"
        self.rows[r].remove(num)
        self.cols[c].remove(num)
        self.boxes[(r // 3, c // 3)].remove(num)

    def move_to_next_cell(self, r: int, c: int) -> Tuple[int, int]:
        # Move to next column
        if c < 8:
            new_r, new_c = r, c + 1
        # Move to next row, reset column index
        else:
            new_r, new_c = r + 1, 0
        return new_r, new_c

    def backtrack(self, r: int, c: int) -> bool:
        # Base case: reached last row + 1
        if r > 8:
            return True

        # If a number already existed in the cell, move to the next cell
        if self.board[r][c] != "0":
            new_r, new_c = self.move_to_next_cell(r, c)
            return self.backtrack(new_r, new_c)

        # If a number can be placed, place it to the board
        for num in self.string_number:
            if self.can_place_number(r, c, num):
                self.place_number_in_cell(r, c, num)
                if self.backtrack(r, c):
                    return True
                else:
                    self.remove_number_in_cell(r, c, num)

        # The sudoku is not solvable
        return False


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
    Solver().print_board(INPUT_BOARD)

    # Solve the Sudoku board
    solution = Solver().sudoku_solver(INPUT_BOARD)

    if solution != INPUT_BOARD:
        print('\nSolution:')
        Solver().print_board(solution)
    else:
        print('\nNot a valid Sudoku board.')
