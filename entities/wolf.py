import pygame as pg
from settings import WOLF_RUN_PATHS, WOLF_ATTACK_PATHS, WOLF_SPEED


class Wolf:
    wolf_run = None
    wolf_attack = None

    def __init__(self):
        if Wolf.wolf_run is None:
            Wolf.wolf_run = [pg.image.load(p).convert_alpha() for p in WOLF_RUN_PATHS]
            Wolf.wolf_attack = [pg.image.load(p).convert_alpha() for p in WOLF_ATTACK_PATHS]
            
        self.rect = Wolf.wolf_run[0].get_rect(topleft=(744, 280))
        self.anim_count = 0

    def update(self):
        self.rect.x -= WOLF_SPEED
    
    def get_rect(self):
        rect = self.rect.copy()
        rect.x += 25
        rect.width -= 50
        rect.y += 25
        rect.height -= 25
        return rect
