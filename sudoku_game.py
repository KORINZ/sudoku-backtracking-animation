import pygame
import sudoku_solver
import sudoku_validator

WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sudoku")
img = pygame.image.load(r'sudoku/icon.png')
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
    cell_space = WIDTH // 9
    WIN.fill(WHITE)

    # Draw existing numbers and their boxes
    for i in range(9):
        for j in range(9):
            if DEFAULT_GRID[i][j] != '0':
                pygame.draw.rect(
                    WIN, GRAY, (i * cell_space, j * cell_space, cell_space, cell_space))
                text1 = FONT.render(str(DEFAULT_GRID[i][j]), True, BLACK)
                WIN.blit(text1, (i * cell_space + cell_space /
                         3.3, j * cell_space + cell_space / 5))

    # Draw board lines
    for i in range(10):
        if i % 3 != 0:
            thickness = 2
        else:
            thickness = 9
        pygame.draw.line(WIN, BLACK, (0, i * cell_space),
                         (WIDTH, i * cell_space), thickness)
        pygame.draw.line(WIN, BLACK, (i * cell_space, 0),
                         (i * cell_space, HEIGHT), thickness)

    pygame.display.update()


def main() -> None:
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board()

    pygame.quit()


if __name__ == "__main__":
    main()
