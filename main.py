import random
import pygame as pg
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WOLF_SPEED,
    WHITE, GRAY, BLUE, ICON_PATH, BG_MUSIC_PATH, FONT_PATH, FONT_SIZE,
)
from world.level import Level
from entities.player import Player
from entities.wolf import Wolf


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("History of Knight")
        icon = pg.image.load(ICON_PATH).convert_alpha()
        pg.display.set_icon(icon)

        Wolf()

        self.level = Level()
        self.player = Player()
        self.heart_image = pg.image.load("assets/images/heart.png").convert_alpha()

        self.wolf_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.wolf_timer, random.randint(1000, 4000))
        self.wolf_list_in_game = []
        self.wolf_anim_count = 0

        bg_sound = pg.mixer.Sound(BG_MUSIC_PATH)
        bg_sound.play(-1)

        self.label = pg.font.Font(FONT_PATH, FONT_SIZE)
        self.label_lose = self.label.render("Вы проиграли!", False, WHITE)
        self.restart_label = self.label.render("Начать заново", False, GRAY)
        self.restart_label_rect = self.restart_label.get_rect(topleft=(150, 230))
        self.gameplay = True

        self.running = True

    def run(self):
        while self.running:
            self.level.draw(self.screen)

            if self.gameplay:
                player_rect = self.player.get_rect()

                if self.wolf_list_in_game:
                    for index in range(len(self.wolf_list_in_game) - 1, -1, -1):
                        wolf = self.wolf_list_in_game[index]

                        wolf.update()

                        if wolf.rect.x < -100:
                            self.wolf_list_in_game.pop(index)
                            continue

                        wolf_rect = wolf.get_rect()

                        if self.player.is_attacking and player_rect.colliderect(wolf_rect):
                            self.wolf_list_in_game.pop(index)  
                            continue

                        if player_rect.colliderect(wolf_rect):
                            if self.player.take_damage():
                                if self.player.health <= 0:
                                    self.gameplay = False
                            self.screen.blit(
                                Wolf.wolf_attack[self.wolf_anim_count % len(Wolf.wolf_attack)],
                                (wolf.rect.x, wolf.rect.y),
                            )

                        else:
                            self.screen.blit(Wolf.wolf_run[self.wolf_anim_count], (wolf.rect.x, wolf.rect.y))

                keys = pg.key.get_pressed()
                self.player.draw(self.screen, keys)
                self.player.update(keys)

                if self.wolf_anim_count == len(Wolf.wolf_run) - 1:
                    self.wolf_anim_count = 0
                self.wolf_anim_count += 1

                self.level.update()
            else:
                self.screen.fill(BLUE)
                self.screen.blit(self.label_lose, (150, 130))
                self.screen.blit(self.restart_label, self.restart_label_rect)

                mouse = pg.mouse.get_pos()
                if self.restart_label_rect.collidepoint(mouse) and pg.mouse.get_pressed()[0]:
                    self.gameplay = True
                    self.player.player_x = 150
                    self.wolf_list_in_game.clear()
            
            for i in range(self.player.health):
                self.screen.blit(self.heart_image, (10 + i * 40, 10))

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == self.wolf_timer:
                    self.wolf_list_in_game.append(Wolf())
                    pg.time.set_timer(self.wolf_timer, random.randint(1500, 4500))
                if event.type == pg.KEYDOWN and event.key == pg.K_f:
                    if self.gameplay:
                        self.player.attack()  
                

            self.clock.tick(FPS)

        pg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()