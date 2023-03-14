import pygame
import sys
import sudoku_solver
from sudoku_validator import sudoku_validator
from typing import Tuple
from copy import deepcopy

# Screen size and board cell size
WIDTH, HEIGHT = 720, 720
CELL_SPACE = WIDTH // 9
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Game title and icon
pygame.display.set_caption("ナンプレ Sudoku")
ICON = pygame.image.load(r'icon.png')
pygame.display.set_icon(ICON)

# Define RGB colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Define fonts
pygame.font.init()
FONT_NUMBER = pygame.font.SysFont("Calibri", 60)
FONT_MENU = pygame.font.Font('ipaexg.ttf', 70)
FONT_BUTTON = pygame.font.Font('ipaexg.ttf', 40)
FONT_BUTTON_SMALL = pygame.font.Font('ipaexg.ttf', 25)
FONT_MESSAGE = pygame.font.Font('ipaexg.ttf', 30)
FONT_MESSAGE_SMALL = pygame.font.Font('ipaexg.ttf', 20)

# Game refresh rate
FPS = 60

# Initial board layout for the game
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


class Menu():
    def __init__(self) -> None:
        self.color = BLACK
        self.font = FONT_BUTTON
        self.line_width = 3
        self.language = '日本語'

    def make_centered_button(self, name: str, starting_y: int) -> Tuple[int, int, int, int]:
        button = self.font.render(name, True, self.color)
        WIN.blit(button, (WIDTH / 2 - button.get_width() // 2, starting_y))

        # Starting x and y points of the button
        button_starting_x, button_starting_y = (
            WIDTH - button.get_width()) // 2, starting_y
        pygame.draw.rect(WIN, BLACK, (button_starting_x, button_starting_y, button.get_width(
        ), button.get_height()), width=self.line_width)

        # Ending x and y points of the button
        button_ending_x, button_ending_y = button_starting_x + \
            button.get_width(), button_starting_y + button.get_height()
        return button_starting_x, button_starting_y, button_ending_x, button_ending_y

    def change_language(self, lang: str, word_ja: str, word_en: str) -> str:
        if lang == self.language:
            return word_ja
        else:
            return word_en

    def make_centered_message(self) -> None:
        pass


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
    '''Highlight current selected cell'''
    for i in range(2):
        pygame.draw.line(WIN, BLACK, (x * CELL_SPACE, (y + i) * CELL_SPACE),
                         (x * CELL_SPACE + CELL_SPACE, (y + i)*CELL_SPACE), 7)
        pygame.draw.line(WIN, BLACK, ((x + i) * CELL_SPACE, y * CELL_SPACE),
                         ((x + i) * CELL_SPACE, y * CELL_SPACE + CELL_SPACE), 7)


def put_number(x: int, y: int, user_input: int) -> None:
    '''Place a number in a cell'''
    number_text = FONT_NUMBER.render(str(user_input), True, BLACK)
    WIN.blit(number_text, (x * CELL_SPACE + CELL_SPACE /
                           3.3, y * CELL_SPACE + CELL_SPACE / 5))


def main() -> None:
    x, y = 0, 0
    language = '日本語'

    while True:
        WIN.fill(WHITE)

        # Place icon image
        menu_icon = pygame.transform.scale(ICON, (120, 120))
        WIN.blit(menu_icon, (WIDTH / 2 - menu_icon.get_width() //
                 2, 75))

        # Place game tittle
        title_lang = Menu().change_language(language, '数独', 'Sudoku')
        title = FONT_MENU.render(title_lang, True, BLACK)
        WIN.blit(title, (WIDTH / 2 - title.get_width() //
                 2, 210))

        # Place language button
        button_language = FONT_BUTTON_SMALL.render('日本語 / ENG', True, BLACK)
        WIN.blit(button_language, (10, 10))
        language_x, language_y = 10, 10

        # Place start button
        if GRID == GRID_COPY:
            start_lang = Menu().change_language(language, 'スタート', 'Start')
            start_x0, start_y0, start_x1, start_y1 = Menu().make_centered_button(start_lang, 400)
        else:
            start_lang = Menu().change_language(language, '続く', 'Continue')
            start_x0, start_y0, start_x1, start_y1 = Menu().make_centered_button(start_lang, 400)

        # Place instruction button
        instruction_lang = Menu().change_language(language, '操作方法', 'How to Play')
        instruction_x0, instruction_y0, instruction_x1, instruction_y1 = Menu(
        ).make_centered_button(instruction_lang, 475)

        # Place setting button
        setting_lang = Menu().change_language(language, '設定', 'Setting')
        setting_x0, setting_y0, setting_x1, setting_y1 = Menu(
        ).make_centered_button(setting_lang, 550)

        # Place quit button
        quit_lang = Menu().change_language(language, '終了', 'Quit')
        quit_x0, quit_y0, quit_x1, quit_y1 = Menu().make_centered_button(quit_lang, 625)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos
            if start_x0 < x < start_x1 and start_y0 < y < start_y1:
                return game()
            if instruction_x0 < x < instruction_x1 and instruction_y0 < y < instruction_y1:
                return instruction()
            if quit_x0 < x < quit_x1 and quit_y0 < y < quit_y1:
                pygame.quit()
                sys.exit()
            if 10 < x < 90 and 10 < y < 40:
                language = '日本語'
            if 110 < x < 170 and 10 < y < 40:
                language = 'ENG'
        pygame.display.update()


def instruction() -> None:
    x, y = 0, 0
    while True:
        WIN.fill(WHITE)

        message_rule = FONT_MESSAGE.render("遊び方", True, BLACK)
        WIN.blit(message_rule, (WIDTH / 2 - message_rule.get_width() // 2, 70))

        message_how_to_play_1 = FONT_MESSAGE_SMALL.render(
            "空いているマスに、キーボードで1〜9のいずれかの数字を入れる。", True, BLACK)
        WIN.blit(message_how_to_play_1, (WIDTH / 2 -
                 message_how_to_play_1.get_width() // 2, 120))

        message_how_to_play_2 = FONT_MESSAGE_SMALL.render(
            "縦・横の各列に、同じ数字が重複して入ってはいけない。", True, BLACK)
        WIN.blit(message_how_to_play_2, (WIDTH / 2 -
                 message_how_to_play_2.get_width() // 2, 150))

        message_how_to_play_3 = FONT_MESSAGE_SMALL.render(
            "太線で囲まれた3x3のグループ内に、同じ数字が重複して入ってはいけない。", True, BLACK)
        WIN.blit(message_how_to_play_3, (WIDTH / 2 -
                 message_how_to_play_3.get_width() // 2, 180))

        message_keyboard = FONT_MESSAGE.render("基本操作", True, BLACK)
        WIN.blit(message_keyboard, (WIDTH / 2 -
                 message_keyboard.get_width() // 2, 250))

        message_esc = FONT_MESSAGE.render(
            "ESC - メニューに戻る（進行状況は保存される）", True, BLACK)
        WIN.blit(message_esc, (WIDTH / 2 - message_esc.get_width() // 2, 300))

        message_d = FONT_MESSAGE.render("D - 現在の数字を消す", True, BLACK)
        WIN.blit(message_d, (WIDTH / 2 - message_d.get_width() // 2, 350))

        # Place go back button
        back_x0, back_y0, back_x1, back_y1 = Menu().make_centered_button('戻り', 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos
            if back_x0 < x < back_x1 and back_y0 < y < back_y1:
                return main()
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
                if event.key == pygame.K_ESCAPE:
                    return main()
                if event.key == pygame.K_d and GRID_COPY[x][y] == '0':
                    GRID[x][y] = '0'

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
