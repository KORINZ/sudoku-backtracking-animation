import pygame
import sudoku_solver
import sudoku_validator


WIDTH, HEIGHT = 720, 720
CELL_SPACE = WIDTH // 9
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sudoku")
img = pygame.image.load(r'icon.png')
pygame.display.set_icon(img)

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

pygame.font.init()
FONT = pygame.font.SysFont("Calibri", 60)

FPS = 60

DEFAULT_GRID = [['5', '3', '0', '0', '7', '0', '0', '0', '0'],
                ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
                ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
                ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
                ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
                ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
                ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
                ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
                ['0', '0', '0', '0', '8', '0', '0', '7', '9']]


def draw_board() -> None:

    # Draw existing numbers and their boxes
    for i in range(9):
        for j in range(9):
            if DEFAULT_GRID[i][j] != '0':
                pygame.draw.rect(
                    WIN, GRAY, (i * CELL_SPACE, j * CELL_SPACE, CELL_SPACE, CELL_SPACE))
                number_text = FONT.render(str(DEFAULT_GRID[i][j]), True, BLACK)
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


def put_number(x: int, y: int, user_input: int) -> None:
    number_text = FONT.render(str(user_input), True, BLACK)
    WIN.blit(number_text, (x * CELL_SPACE + CELL_SPACE /
                           3.3, y * CELL_SPACE + CELL_SPACE / 5))


def main() -> None:
    clock = pygame.time.Clock()
    run = True
    user_input = 0
    x, y = 0, 0
    WIN.fill(WHITE)

    while run:
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
            if user_input != 0:
                put_number(x, y, user_input)
                print(x, y)

        draw_board()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
