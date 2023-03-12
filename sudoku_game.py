import pygame
import sys
import sudoku_solver
from sudoku_validator import sudoku_validator

from copy import deepcopy


WIDTH, HEIGHT = 720, 720
CELL_SPACE = WIDTH // 9
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sudoku")
ICON = pygame.image.load(r'icon.png')
pygame.display.set_icon(ICON)

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

pygame.font.init()
FONT_NUMBER = pygame.font.SysFont("Calibri", 60)
FONT_MENU = pygame.font.Font('ipaexg.ttf', 70)
FONT_BUTTON = pygame.font.Font('ipaexg.ttf', 40)
FONT_MESSAGE = pygame.font.Font('ipaexg.ttf', 30)

FPS = 60

GRID = [['5', '3', '0', '0', '7', '0', '0', '0', '0'],
        ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
        ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
        ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
        ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
        ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
        ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
        ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
        ['0', '0', '0', '0', '8', '0', '0', '7', '9']]

GRID_COPY = deepcopy(GRID)


def draw_board() -> None:

    # Draw existing numbers and their boxes

    for i in range(9):
        for j in range(9):
            if GRID[i][j] == GRID_COPY[i][j]:
                cell_color = GRAY
            else:
                cell_color = WHITE
            if GRID[i][j] != '0':
                pygame.draw.rect(WIN, cell_color, (i * CELL_SPACE,
                                                   j * CELL_SPACE, CELL_SPACE, CELL_SPACE))
                number_text = FONT_NUMBER.render(str(GRID[i][j]), True, BLACK)
                WIN.blit(number_text, (i * CELL_SPACE + CELL_SPACE /
                                       3.3, j * CELL_SPACE + CELL_SPACE / 5))

    # Draw board lines
    for i in range(10):
        if i % 3 != 0:
            thickness = 2
        else:
            thickness = 9
        pygame.draw.line(WIN, BLACK, (0, i * CELL_SPACE),
                         (WIDTH, i * CELL_SPACE), thickness)
        pygame.draw.line(WIN, BLACK, (i * CELL_SPACE, 0),
                         (i * CELL_SPACE, HEIGHT), thickness)


def highlight_selection(x: int, y: int) -> None:
    for i in range(2):
        pygame.draw.line(WIN, BLACK, (x * CELL_SPACE, (y + i) * CELL_SPACE),
                         (x * CELL_SPACE + CELL_SPACE, (y + i)*CELL_SPACE), 7)
        pygame.draw.line(WIN, BLACK, ((x + i) * CELL_SPACE, y * CELL_SPACE),
                         ((x + i) * CELL_SPACE, y * CELL_SPACE + CELL_SPACE), 7)


def put_number(x: int, y: int, user_input: int) -> None:
    number_text = FONT_NUMBER.render(str(user_input), True, BLACK)
    WIN.blit(number_text, (x * CELL_SPACE + CELL_SPACE /
                           3.3, y * CELL_SPACE + CELL_SPACE / 5))


def main() -> None:
    while True:
        WIN.fill(WHITE)
        menu_icon = pygame.transform.scale(ICON, (100, 100))
        WIN.blit(menu_icon, (WIDTH / 2 - menu_icon.get_width() //
                 2, 75))
        title = FONT_MENU.render("数独", True, BLACK)
        WIN.blit(title, (WIDTH / 2 - title.get_width() //
                 2, 200))

        message = FONT_MESSAGE.render(
            "Press Any Key to Start...", True, BLACK)
        WIN.blit(message, (WIDTH / 2 - message.get_width() //
                 2, 300))

        button_start = FONT_BUTTON.render("開始", True, BLACK)
        WIN.blit(button_start, (WIDTH / 2 - button_start.get_width() //
                 2, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game()
                sys.exit()
        pygame.display.update()


def game() -> None:
    clock = pygame.time.Clock()
    run = True
    user_input = 0
    x, y = 0, 0

    while run:
        WIN.fill(WHITE)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                x = pos[0] // CELL_SPACE
                y = pos[1] // CELL_SPACE

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    user_input = 1
                if event.key == pygame.K_2:
                    user_input = 2
                if event.key == pygame.K_3:
                    user_input = 3
                if event.key == pygame.K_4:
                    user_input = 4
                if event.key == pygame.K_5:
                    user_input = 5
                if event.key == pygame.K_6:
                    user_input = 6
                if event.key == pygame.K_7:
                    user_input = 7
                if event.key == pygame.K_8:
                    user_input = 8
                if event.key == pygame.K_9:
                    user_input = 9

        if user_input != 0 and GRID_COPY[x][y] == '0':

            GRID[x][y] = str(user_input)

            if sudoku_validator(GRID):
                put_number(x, y, user_input)
            else:
                GRID[x][y] = "0"

            # reset user_input to 0 after put_number() and sudoku_validator()
            user_input = 0
            print(x, y)

        draw_board()
        highlight_selection(x, y)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
