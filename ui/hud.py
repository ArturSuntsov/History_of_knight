import pygame as pg

from settings import (
    FONT_PATH,
    FONT_SIZE,
    HEART_PATH,
    HEART_SPACING,
    HEART_START_X,
    HEART_START_Y,
    SCORE_TEXT_X,
    SCORE_TEXT_Y,
    WHITE,
    WOLF_FACE_PATH,
    WOLF_ICON_X,
    WOLF_ICON_Y,
)


class HUD:
    """Индикаторы здоровья и счёта убитых волков."""

    def __init__(self):
        self.heart_image = pg.image.load(HEART_PATH).convert_alpha()
        self.wolf_icon = pg.image.load(WOLF_FACE_PATH).convert_alpha()
        self.font = pg.font.Font(FONT_PATH, FONT_SIZE)

    def draw(self, screen, health, wolves_killed):
        for index in range(health):
            x = HEART_START_X + index * HEART_SPACING
            screen.blit(self.heart_image, (x, HEART_START_Y))

        screen.blit(self.wolf_icon, (WOLF_ICON_X, WOLF_ICON_Y))
        score_text = self.font.render(str(wolves_killed), False, WHITE)
        screen.blit(score_text, (SCORE_TEXT_X, SCORE_TEXT_Y))
