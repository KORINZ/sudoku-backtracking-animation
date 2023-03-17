import pygame
import sys
from sudoku_menu import Menu
from sudoku_solver import Solver
from sudoku_game_board import GameBoard
from sudoku_grid_numbers import GRID, GRID_COPY

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

# Game initial settings
FPS = 60
DELAY_TIME = 1  # ミリ秒
HIGHLIGHT_COLOR = BLACK
menu = Menu()
game_board = GameBoard()


def main(language='日本語') -> None:
    x, y = 0, 0

    while True:
        WIN.fill(WHITE)

        # Place icon image
        menu_icon = pygame.transform.scale(ICON, (120, 120))
        WIN.blit(menu_icon, (WIDTH / 2 - menu_icon.get_width() //
                             2, 75))

        # Place game tittle
        title_lang = menu.change_language(language, '数独', 'Sudoku')
        title = FONT_MENU.render(title_lang, True, BLACK)
        WIN.blit(title, (WIDTH / 2 - title.get_width() //
                         2, 210))

        # Place language button
        button_language = FONT_BUTTON_SMALL.render('日本語 / ENG', True, BLACK)
        WIN.blit(button_language, (10, 10))
        language_x, language_y = 10, 10

        # Place start button
        if GRID == GRID_COPY:
            start_lang = menu.change_language(language, 'スタート', 'Start')
            start_x0, start_y0, start_x1, start_y1 = menu.make_centered_button(
                start_lang, 400)
        else:
            start_lang = menu.change_language(language, '続く', 'Continue')
            start_x0, start_y0, start_x1, start_y1 = menu.make_centered_button(
                start_lang, 400)

        # Place instruction button
        instruction_lang = menu.change_language(
            language, '操作方法', 'How to Play')
        instruction_x0, instruction_y0, instruction_x1, instruction_y1 = menu.make_centered_button(
            instruction_lang, 475)

        # Place setting button
        setting_lang = menu.change_language(language, '設定', 'Setting')
        setting_x0, setting_y0, setting_x1, setting_y1 = menu.make_centered_button(
            setting_lang, 550)

        # Place quit button
        quit_lang = menu.change_language(language, '終了', 'Quit')
        quit_x0, quit_y0, quit_x1, quit_y1 = menu.make_centered_button(
            quit_lang, 625)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos
            if start_x0 < x < start_x1 and start_y0 < y < start_y1:
                return game()
            if instruction_x0 < x < instruction_x1 and instruction_y0 < y < instruction_y1:
                return instruction(language)
            if setting_x0 < x < setting_x1 and setting_y0 < y < setting_y1:
                return setting(language)
            if quit_x0 < x < quit_x1 and quit_y0 < y < quit_y1:
                pygame.quit()
                sys.exit()
            if 10 < x < 90 and 10 < y < 40:
                language = '日本語'
            if 110 < x < 170 and 10 < y < 40:
                language = 'ENG'
        pygame.display.update()


def instruction(language: str) -> None:
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

        message_sr = FONT_MESSAGE.render("SHIFT + R - リセット", True, BLACK)
        WIN.blit(message_sr, (WIDTH / 2 - message_sr.get_width() // 2, 400))

        message_sb = FONT_MESSAGE.render(
            "SHIFT + B - バックトラッキング動画", True, BLACK)
        WIN.blit(message_sb, (WIDTH / 2 - message_sb.get_width() // 2, 450))

        message_ss = FONT_MESSAGE.render("SHIFT + S - 解答を表示", True, BLACK)
        WIN.blit(message_ss, (WIDTH / 2 - message_ss.get_width() // 2, 500))

        # Place go back button
        back_lang = menu.change_language(language, '戻る', 'Back')
        back_x0, back_y0, back_x1, back_y1 = menu.make_centered_button(
            back_lang, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main(language='ENG') if back_lang == 'Back' else main()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos
            if back_x0 < x < back_x1 and back_y0 < y < back_y1:
                return main(language='ENG') if back_lang == 'Back' else main()
        pygame.display.update()


def setting(language: str) -> None:
    x, y = 0, 0
    while True:
        WIN.fill(WHITE)

        message_dummy = FONT_MESSAGE.render("まだ何もない", True, BLACK)
        WIN.blit(message_dummy, (WIDTH / 2 - message_dummy.get_width() // 2, 70))

        # Place go back button
        back_lang = menu.change_language(language, '戻る', 'Back')
        back_x0, back_y0, back_x1, back_y1 = menu.make_centered_button(
            back_lang, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main(language='ENG') if back_lang == 'Back' else main()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos
            if back_x0 < x < back_x1 and back_y0 < y < back_y1:
                return main(language='ENG') if back_lang == 'Back' else main()
        pygame.display.update()


def game() -> None:
    clock = pygame.time.Clock()
    run = True
    user_input = 0
    x_col, y_row = 0, 0

    while run:
        WIN.fill(WHITE)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                x_col, y_row = pos[0] // CELL_SPACE, pos[1] // CELL_SPACE

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
                if event.key == pygame.K_d and GRID_COPY[y_row][x_col] == 0:
                    GRID[y_row][x_col] = 0
                if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    for i in range(9):
                        for j in range(9):
                            GRID[i][j] = GRID_COPY[i][j]
                if event.key == pygame.K_b and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    game_board.backtracking_solver(GRID, 0, 0)

                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    solution = Solver().sudoku_solver(GRID_COPY)
                    for i in range(9):
                        for j in range(9):
                            GRID[i][j] = solution[i][j]

        # Check if current cell is occupied
        if game_board.is_valid_move(GRID, y_row, x_col, user_input) and GRID_COPY[y_row][x_col] == 0 and user_input != 0:
            GRID[y_row][x_col] = user_input
            game_board.put_number(y_row, x_col, user_input)

            # Reset user_input to 0
            user_input = 0

        game_board.draw_board()
        game_board.highlight_selection(y_row, x_col)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
