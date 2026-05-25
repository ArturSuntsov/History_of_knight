import pygame as pg

from core.geometry import apply_hitbox
from settings import (
    WOLF_DESPAWN_X,
    WOLF_HITBOX_HEIGHT_REDUCE,
    WOLF_HITBOX_WIDTH_REDUCE,
    WOLF_HITBOX_X_OFFSET,
    WOLF_HITBOX_Y_OFFSET,
    WOLF_SPEED,
    WOLF_SPRITE_HEIGHT,
    WOLF_SPRITE_WIDTH,
    WOLF_SPAWN_X,
    WOLF_SPAWN_Y,
)


class WolfModel:
    """Состояние и движение волка без отрисовки."""

    def __init__(self):
        self.x = WOLF_SPAWN_X
        self.y = WOLF_SPAWN_Y
        self.attacking = False

    def update(self):
        self.x -= WOLF_SPEED

    def should_despawn(self):
        return self.x < WOLF_DESPAWN_X

    def get_rect(self):
        base = pg.Rect(self.x, self.y, WOLF_SPRITE_WIDTH, WOLF_SPRITE_HEIGHT)
        return apply_hitbox(
            base,
            WOLF_HITBOX_X_OFFSET,
            WOLF_HITBOX_WIDTH_REDUCE,
            WOLF_HITBOX_Y_OFFSET,
            WOLF_HITBOX_HEIGHT_REDUCE,
        )
