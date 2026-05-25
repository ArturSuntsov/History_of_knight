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

    def add_wolf(self):
        self.wolves.append(WolfModel())

    def update_player(self, keys):
        self.player.update(keys)

    def update_wolves(self):
        player_rect = self.player.get_rect()

        for index in range(len(self.wolves) - 1, -1, -1):
            wolf = self.wolves[index]
            wolf.attacking = False
            wolf.update()

            if wolf.should_despawn():
                self.wolves.pop(index)
                continue

            wolf_rect = wolf.get_rect()

            if self.player.is_attacking and player_rect.colliderect(wolf_rect):
                self.wolves_killed += 1
                self.wolves.pop(index)
                continue

            if player_rect.colliderect(wolf_rect):
                self.player.take_damage()
                if self.player.health <= 0:
                    self.gameplay = False
                wolf.attacking = True

    def advance_wolf_animation(self):
        self.wolf_anim_frame = (self.wolf_anim_frame + 1) % self.wolf_anim_frame_count

    def reset(self):
        self.player.reset()
        self.wolves.clear()
        self.wolves_killed = 0
        self.gameplay = True
        self.wolf_anim_frame = 0
