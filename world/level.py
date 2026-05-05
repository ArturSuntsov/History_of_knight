import pygame as pg
from settings import BG_PATH


class Level:
    def __init__(self):
        self.bg = pg.image.load(BG_PATH).convert_alpha()
        self.bg_x = 0

    def update(self):
        self.bg_x -= 3
        if self.bg_x <= -740:
            self.bg_x = 0

    def draw(self, screen):
        screen.blit(self.bg, (self.bg_x, 0))
        screen.blit(self.bg, (self.bg_x + 740, 0))