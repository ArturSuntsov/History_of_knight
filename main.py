import random

import pygame as pg

from core.game_state import GameState
from core.input_handler import InputHandler
from level import LevelModel, LevelView
from player import PlayerView
from settings import (
    BG_MUSIC_PATH,
    FPS,
    ICON_PATH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WOLF_SPAWN_INITIAL_MAX,
    WOLF_SPAWN_INITIAL_MIN,
)
from ui import GameOverView, HUD
from wolf import WolfView


class Game:
    """Контроллер: связывает модели, представления и ввод."""

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("History of Knight")
        pg.display.set_icon(pg.image.load(ICON_PATH).convert_alpha())

        self.state = GameState()
        self.level = LevelModel()
        self.level_view = LevelView()
        self.player_view = PlayerView()
        self.wolf_view = WolfView()
        self.hud = HUD()
        self.game_over_view = GameOverView()
        self.input_handler = InputHandler()

        self.wolf_timer = pg.USEREVENT + 1
        pg.time.set_timer(
            self.wolf_timer,
            random.randint(WOLF_SPAWN_INITIAL_MIN, WOLF_SPAWN_INITIAL_MAX),
        )

        pg.mixer.Sound(BG_MUSIC_PATH).play(-1)
        self.running = True

    def _spawn_wolf(self):
        self.state.add_wolf()
        pg.time.set_timer(
            self.wolf_timer,
            self.state.difficulty_manager.get_spawn_delay(),
        )

    def _render_gameplay(self):
        keys = self.input_handler.get_pressed_keys()
        self.state.update_player(keys)
        self.state.update_wolves()
        self.state.advance_wolf_animation()

        for wolf in self.state.wolves:
            self.wolf_view.draw(self.screen, wolf, self.state.wolf_anim_frame)

        self.hud.draw(self.screen, self.state.player.health, self.state.wolves_killed)
        self.player_view.draw(self.screen, self.state.player, keys)
        self.level.update()

    def quit_game(self):
        self.running = False

    def run(self):
        while self.running:
            self.level_view.draw(self.screen, self.level)

            if self.state.gameplay:
                self._render_gameplay()
            else:
                self.game_over_view.draw(self.screen, self.state.wolves_killed)
                if self.input_handler.is_mouse_clicked(self.game_over_view.restart_rect):
                    self.state.reset()
                    self.level.reset()

            pg.display.update()
            self.input_handler.process_events(
                self.wolf_timer,
                self.state.gameplay,
                on_quit=self.quit_game,
                on_spawn_wolf=self._spawn_wolf,
                on_attack=self.state.player.attack,
            )
            self.clock.tick(FPS)

        pg.quit()


if __name__ == "__main__":
    Game().run()