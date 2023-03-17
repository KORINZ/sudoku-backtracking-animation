import pygame
from sudoku_grid_numbers import GRID, GRID_COPY
from sudoku_solver import Solver
from typing import List
import sys

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = BLACK
DELAY_TIME = 1


class GameBoard:
    def __init__(self) -> None:
        self.WIN = pygame.display.get_surface()
        self.WIDTH = pygame.display.get_surface().get_size()[0]
        self.HEIGHT = pygame.display.get_surface().get_size()[1]
        self.CELL_SPACE = self.WIDTH // 9
        self.FONT_NUMBER = pygame.font.SysFont("Calibri", 60)

    def draw_board(self) -> None:
        """Draw existing numbers and their boxes"""
        for i in range(9):
            for j in range(9):
                if GRID[i][j] == GRID_COPY[i][j]:
                    cell_color = GRAY
                else:
                    cell_color = WHITE
                if GRID[i][j] != 0:
                    pygame.draw.rect(self.WIN, cell_color, (j * self.CELL_SPACE,
                                                            i * self.CELL_SPACE, self.CELL_SPACE, self.CELL_SPACE))

                    number_text = self.FONT_NUMBER.render(
                        str(GRID[i][j]), True, BLACK)
                    y_row, x_col = j * self.CELL_SPACE + self.CELL_SPACE / \
                        3.2, i * self.CELL_SPACE + self.CELL_SPACE / 5
                    self.WIN.blit(number_text, (y_row, x_col))

        # Draw board lines
        for i in range(10):
            if i % 3 != 0:
                thickness = 2
            else:
                thickness = 9
            pygame.draw.line(self.WIN, BLACK, (0, i * self.CELL_SPACE),
                             (self.WIDTH, i * self.CELL_SPACE), thickness)
            pygame.draw.line(self.WIN, BLACK, (i * self.CELL_SPACE, 0),
                             (i * self.CELL_SPACE, self.HEIGHT), thickness)

    def highlight_selection(self, x_col: int, y_row: int) -> None:
        '''Highlight current selected cell'''
        for i in range(2):
            pygame.draw.line(self.WIN, HIGHLIGHT_COLOR, (y_row * self.CELL_SPACE, (x_col + i) * self.CELL_SPACE),
                             (y_row * self.CELL_SPACE + self.CELL_SPACE, (x_col + i) * self.CELL_SPACE), 7)
            pygame.draw.line(self.WIN, HIGHLIGHT_COLOR, ((y_row + i) * self.CELL_SPACE, x_col * self.CELL_SPACE),
                             ((y_row + i) * self.CELL_SPACE, x_col * self.CELL_SPACE + self.CELL_SPACE), 7)

    def put_number(self, x_col: int, y_row: int, user_input: int) -> None:
        '''Place a number in a cell'''
        number_text = self.FONT_NUMBER.render(str(user_input), True, BLACK)
        self.WIN.blit(number_text, (y_row * self.CELL_SPACE + self.CELL_SPACE /
                                    3.2, x_col * self.CELL_SPACE + self.CELL_SPACE / 5))

    def is_valid_move(self, grid: List[List[int]], r: int, c: int, num: int) -> bool:
        """Check if a number is valid in current location"""

        # Check current row and current column
        for _ in range(9):
            if grid[r][_] == num:
                return False
            if grid[_][c] == num:
                return False

        # Check box
        i = r // 3
        j = c // 3
        for r in range(i * 3, i * 3 + 3):
            for c in range(j * 3, j * 3 + 3):
                if grid[r][c] == num:
                    return False
        return True

    def backtracking_solver(self, grid: List[List[int]], r: int, c: int) -> bool:
        """Solve the grid with backtracking animation"""

        while grid[r][c] != 0:
            r, c = Solver().move_to_next_cell(r, c)

            # Base case
            if r > 8:
                return True

        pygame.event.pump()

        for num in range(1, 10):
            if self.is_valid_move(grid, r, c, num):
                grid[r][c] = num

                # Refresh Sudoku board
                self.WIN.fill(WHITE)
                self.draw_board()
                self.highlight_selection(r, c)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)

                if self.backtracking_solver(grid, r, c):
                    return True
                else:
                    grid[r][c] = 0

                # Refresh Sudoku board
                self.WIN.fill(WHITE)
                self.draw_board()
                self.highlight_selection(r, c)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        # Stop and reset grid
                        if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            for i in range(9):
                                for j in range(9):
                                    GRID[i][j] = GRID_COPY[i][j]
                            return True
        return False
