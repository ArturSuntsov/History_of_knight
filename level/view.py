import pygame as pg

from settings import BG_PATH, SCREEN_WIDTH


class LevelView:
    """Отрисовка фонового изображения."""

    def __init__(self):
        self.bg = pg.image.load(BG_PATH).convert_alpha()

    def draw(self, screen, level):
        screen.blit(self.bg, (level.bg_x, 0))
        screen.blit(self.bg, (level.bg_x + SCREEN_WIDTH, 0))
