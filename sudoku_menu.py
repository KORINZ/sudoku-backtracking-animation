import pygame
from typing import Tuple

WIDTH, HEIGHT = 720, 720


class Menu():
    def __init__(self) -> None:
        self.WIDTH = 720
        self.HEIGHT = 720
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.color = (0, 0, 0)
        self.font = pygame.font.Font('ipaexg.ttf', 40)
        self.line_width = 3
        self.language = '日本語'

    def make_centered_button(self, name: str, starting_y: int) -> Tuple[int, int, int, int]:
        button = self.font.render(name, True, self.color)
        self.WIN.blit(
            button, (WIDTH / 2 - button.get_width() // 2, starting_y))

        # Starting x and y points of the button
        button_starting_x, button_starting_y = (
            WIDTH - button.get_width()) // 2, starting_y
        pygame.draw.rect(self.WIN, self.color, (button_starting_x, button_starting_y, button.get_width(
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
