import pygame as pg
from settings import PLAYER_RIGHT_PATHS, PLAYER_LEFT_PATHS, PLAYER_SPEED, PLAYER_ATTACK_PATHS


class Player:
    def __init__(self):
        self.run_left = [pg.image.load(p).convert_alpha() for p in PLAYER_LEFT_PATHS]
        self.run_right = [pg.image.load(p).convert_alpha() for p in PLAYER_RIGHT_PATHS]
        self.attack_sprites = [pg.image.load(p).convert_alpha() for p in PLAYER_ATTACK_PATHS]
        self.is_attacking = False
        self.attack_anim_count = 0

        self.player_x = 150
        self.player_y = 230
        self.player_speed = PLAYER_SPEED
        self.player_anim_count = 0

        self.is_jump = False
        self.jump_count = 10

        self.attack_cooldown = 0 

        self.health = 3
        self.invincible_timer = 0
        self.invincible_duration = 30
    
    def attack(self):
        if self.attack_cooldown <= 0 and not self.is_attacking:
            self.is_attacking = True
            self.attack_anim_count = 0
            self.attack_cooldown = 15
    
    def take_damage(self):
        if self.invincible_timer <= 0:
            self.health -= 1
            self.invincible_timer = self.invincible_duration
            return True
        return False

    def update(self, keys):
        if keys[pg.K_LEFT] and self.player_x > 0:
            self.player_x -= self.player_speed
        elif keys[pg.K_RIGHT] and self.player_x < 200:
            self.player_x += self.player_speed

        if not self.is_jump:
            if keys[pg.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -10:
                if self.jump_count > 0:
                    self.player_y -= (self.jump_count ** 2) / 2
                else:
                    self.player_y += (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10

        if self.player_anim_count == len(self.run_left) - 1:
            self.player_anim_count = 0
        self.player_anim_count += 1
        
        if self.is_attacking:
            if self.attack_anim_count >= len(self.attack_sprites) - 1:
                self.is_attacking = False
            else:
                self.attack_anim_count += 1
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def draw(self, screen, keys):
        if self.invincible_timer > 0 and (self.invincible_timer // 5) % 2 == 0:
            return
        
        if self.is_attacking:
            screen.blit(self.attack_sprites[self.attack_anim_count], 
                       (self.player_x, self.player_y))
        elif keys[pg.K_LEFT]:
            screen.blit(self.run_left[self.player_anim_count], (self.player_x, self.player_y))
        else:
            screen.blit(self.run_right[self.player_anim_count], (self.player_x, self.player_y))

    def get_rect(self):
        rect = self.run_left[0].get_rect(topleft=(self.player_x, self.player_y))
        rect.x += 58
        rect.width -= 120
        rect.y += 53
        rect.height -= 107
        return rect
