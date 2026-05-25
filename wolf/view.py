import pygame as pg

from settings import WOLF_ATTACK_PATHS, WOLF_RUN_PATHS


class WolfView:
    """Отрисовка анимаций волка."""

    _run_sprites = None
    _attack_sprites = None

    def __init__(self):
        if WolfView._run_sprites is None:
            WolfView._run_sprites = [pg.image.load(path).convert_alpha() for path in WOLF_RUN_PATHS]
            WolfView._attack_sprites = [pg.image.load(path).convert_alpha() for path in WOLF_ATTACK_PATHS]

    def draw(self, screen, wolf, anim_frame):
        if wolf.attacking:
            sprites = self._attack_sprites
            frame = anim_frame % len(sprites)
        else:
            sprites = self._run_sprites
            frame = anim_frame % len(sprites)

        screen.blit(sprites[frame], (wolf.x, wolf.y))
