import pygame as pg

from core.geometry import apply_hitbox
from settings import (
    JUMP_COUNT,
    JUMP_THRESHOLD,
    PLAYER_ATTACK_COOLDOWN,
    PLAYER_BLINK_INTERVAL,
    PLAYER_HEALTH,
    PLAYER_HITBOX_HEIGHT_REDUCE,
    PLAYER_HITBOX_WIDTH_REDUCE,
    PLAYER_HITBOX_X_OFFSET,
    PLAYER_HITBOX_Y_OFFSET,
    PLAYER_INVINCIBLE_DURATION,
    PLAYER_MAX_X,
    PLAYER_SPEED,
    PLAYER_SPRITE_HEIGHT,
    PLAYER_SPRITE_WIDTH,
    PLAYER_START_X,
    PLAYER_START_Y,
)


class PlayerModel:
    """Состояние и логика игрока без отрисовки."""

    ATTACK_FRAME_COUNT = 6
    RUN_FRAME_COUNT = 8

    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.speed = PLAYER_SPEED
        self.run_anim_frame = 0
        self.is_attacking = False
        self.attack_anim_frame = 0
        self.is_jumping = False
        self.jump_count = JUMP_COUNT
        self.attack_cooldown = 0
        self.health = PLAYER_HEALTH
        self.invincible_timer = 0

    def attack(self):
        if self.attack_cooldown <= 0 and not self.is_attacking:
            self.is_attacking = True
            self.attack_anim_frame = 0
            self.attack_cooldown = PLAYER_ATTACK_COOLDOWN

    def take_damage(self):
        if self.invincible_timer > 0:
            return False
        self.health -= 1
        self.invincible_timer = PLAYER_INVINCIBLE_DURATION
        return True

    def is_visible(self):
        if self.invincible_timer <= 0:
            return True
        return (self.invincible_timer // PLAYER_BLINK_INTERVAL) % 2 != 0

    def update(self, keys):
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= self.speed
        elif keys[pg.K_RIGHT] and self.x < PLAYER_MAX_X:
            self.x += self.speed

        if not self.is_jumping:
            if keys[pg.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= JUMP_THRESHOLD:
                if self.jump_count > 0:
                    self.y -= (self.jump_count ** 2) / 2
                else:
                    self.y += (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = JUMP_COUNT

        self.run_anim_frame = (self.run_anim_frame + 1) % self.RUN_FRAME_COUNT

        if self.is_attacking:
            if self.attack_anim_frame >= self.ATTACK_FRAME_COUNT - 1:
                self.is_attacking = False
            else:
                self.attack_anim_frame += 1

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def get_rect(self):
        base = pg.Rect(self.x, self.y, PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)
        return apply_hitbox(
            base,
            PLAYER_HITBOX_X_OFFSET,
            PLAYER_HITBOX_WIDTH_REDUCE,
            PLAYER_HITBOX_Y_OFFSET,
            PLAYER_HITBOX_HEIGHT_REDUCE,
        )

    def reset(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.health = PLAYER_HEALTH
        self.invincible_timer = 0
        self.is_attacking = False
        self.attack_cooldown = 0
        self.is_jumping = False
        self.jump_count = JUMP_COUNT
