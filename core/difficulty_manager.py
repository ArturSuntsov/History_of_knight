import random

from settings import (
    DIFFICULTY_MAX,
    DIFFICULTY_MIN,
    WOLF_SPEED,
    WOLF_SPAWN_MAX_TIME,
    WOLF_SPAWN_MIN_TIME,
    DIFFICULTY_DECREASE_STEP,
    DIFFICULTY_INCREASE_STEP,
    DIFFICULTY_DEATH_THRESHOLD,
    DIFFICULTY_WOLF_THRESHOLD,
)


class DifficultyManager:
    """Управляет динамической сложностью."""

    def __init__(self):
        self.difficulty_multiplier = 1.0
        self.wolves_killed_this_run = 0
        self.frames_survived = 0

    def update(self):
        self.frames_survived += 1

    def on_wolf_killed(self):
        self.wolves_killed_this_run += 1

    def on_player_died(self):
        if self.wolves_killed_this_run < DIFFICULTY_DEATH_THRESHOLD:
            self.difficulty_multiplier = max(DIFFICULTY_MIN, self.difficulty_multiplier - DIFFICULTY_DECREASE_STEP)
        elif self.wolves_killed_this_run > DIFFICULTY_WOLF_THRESHOLD:
            self.difficulty_multiplier = min(DIFFICULTY_MAX, self.difficulty_multiplier + DIFFICULTY_INCREASE_STEP)

    def reset_for_new_run(self):
        self.wolves_killed_this_run = 0
        self.frames_survived = 0

    def get_wolf_speed(self):
        return WOLF_SPEED * self.difficulty_multiplier

    def get_spawn_delay(self):
        return int(random.randint(WOLF_SPAWN_MIN_TIME, WOLF_SPAWN_MAX_TIME) / self.difficulty_multiplier)