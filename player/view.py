import pygame as pg

from settings import PLAYER_ATTACK_PATHS, PLAYER_LEFT_PATHS, PLAYER_RIGHT_PATHS


class PlayerView:
    """Отрисовка спрайтов игрока по состоянию модели."""

    def __init__(self):
        self.run_left = [pg.image.load(path).convert_alpha() for path in PLAYER_LEFT_PATHS]
        self.run_right = [pg.image.load(path).convert_alpha() for path in PLAYER_RIGHT_PATHS]
        self.attack_sprites = [pg.image.load(path).convert_alpha() for path in PLAYER_ATTACK_PATHS]

    def draw(self, screen, player, keys):
        if not player.is_visible():
            return

        if player.is_attacking:
            sprite = self.attack_sprites[player.attack_anim_frame]
        elif keys[pg.K_LEFT]:
            sprite = self.run_left[player.run_anim_frame]
        else:
            sprite = self.run_right[player.run_anim_frame]

        screen.blit(sprite, (player.x, player.y))
