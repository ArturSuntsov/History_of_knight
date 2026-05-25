import pygame as pg

from settings import (
    FONT_PATH,
    FONT_SIZE,
    GAME_OVER_TEXT_X,
    GAME_OVER_TEXT_Y,
    GRAY,
    RESTART_BUTTON_X,
    RESTART_BUTTON_Y,
    SCORE_KILLS_X,
    SCORE_KILLS_Y,
    WHITE,
    DARK_GRAY,
)


class GameOverView:
    """Экран проигрыша и кнопка перезапуска."""

    def __init__(self):
        self.font = pg.font.Font(FONT_PATH, FONT_SIZE)
        self.lose_text = self.font.render("Вы проиграли!", False, WHITE)
        self.restart_label = self.font.render("Начать заново", False, GRAY)
        self.restart_rect = self.restart_label.get_rect(topleft=(RESTART_BUTTON_X, RESTART_BUTTON_Y))

    def draw(self, screen, wolves_killed):
        screen.fill(DARK_GRAY)
        screen.blit(self.lose_text, (GAME_OVER_TEXT_X, GAME_OVER_TEXT_Y))
        screen.blit(self.restart_label, self.restart_rect)
        kills_text = self.font.render(f"Убито волков: {wolves_killed}", False, WHITE)
        screen.blit(kills_text, (SCORE_KILLS_X, SCORE_KILLS_Y))
