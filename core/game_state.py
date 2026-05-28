from core.difficulty_manager import DifficultyManager
from player.model import PlayerModel
from settings import WOLF_RUN_PATHS
from wolf.model import WolfModel


class GameState:
    """Игровая логика: коллизии, счёт, список врагов."""

    def __init__(self):
        self.player = PlayerModel()
        self.wolves = []
        self.wolves_killed = 0
        self.gameplay = True
        self.wolf_anim_frame = 0
        self.wolf_anim_frame_count = len(WOLF_RUN_PATHS)
        self.difficulty_manager = DifficultyManager()

    def add_wolf(self):
        self.wolves.append(WolfModel())

    def update_player(self, keys):
        self.player.update(keys)

    def update_wolves(self):
        wolf_speed = self.difficulty_manager.get_wolf_speed()
        player_rect = self.player.get_rect()
        player_died = False

        for index in range(len(self.wolves) - 1, -1, -1):
            wolf = self.wolves[index]
            wolf.attacking = False
            wolf.x -= wolf_speed

            if wolf.should_despawn():
                self.wolves.pop(index)
                continue

            wolf_rect = wolf.get_rect()

            if self.player.is_attacking and player_rect.colliderect(wolf_rect):
                self.difficulty_manager.on_wolf_killed()
                self.wolves_killed += 1
                self.wolves.pop(index)
                continue

            if player_rect.colliderect(wolf_rect):
                damage_dealt = self.player.take_damage()
                if damage_dealt and self.player.health <= 0:
                    self.gameplay = False
                    player_died = True
                wolf.attacking = True

        self.difficulty_manager.update()
        if player_died:
            self.difficulty_manager.on_player_died()

    def advance_wolf_animation(self):
        self.wolf_anim_frame = (self.wolf_anim_frame + 1) % self.wolf_anim_frame_count

    def reset(self):
        self.player.reset()
        self.wolves.clear()
        self.wolves_killed = 0
        self.gameplay = True
        self.wolf_anim_frame = 0
        self.difficulty_manager.reset_for_new_run()
