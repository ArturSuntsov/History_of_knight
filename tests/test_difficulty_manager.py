import unittest

from core.difficulty_manager import DifficultyManager
from settings import (
    DIFFICULTY_MAX,
    DIFFICULTY_MIN,
    WOLF_SPEED,
    WOLF_SPAWN_MAX_TIME,
    WOLF_SPAWN_MIN_TIME,
)


class DifficultyManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = DifficultyManager()

    def test_initial_multiplier(self):
        self.assertEqual(self.manager.difficulty_multiplier, 1.0)

    def test_kill_registration(self):
        self.assertEqual(self.manager.wolves_killed_this_run, 0)
        self.manager.on_wolf_killed()
        self.assertEqual(self.manager.wolves_killed_this_run, 1)
        self.manager.on_wolf_killed()
        self.assertEqual(self.manager.wolves_killed_this_run, 2)

    def test_death_decreases_difficulty_when_kills_below_threshold(self):
        for _ in range(2):
            self.manager.on_wolf_killed()
        self.manager.on_player_died()
        self.assertEqual(self.manager.difficulty_multiplier, 0.8)

    def test_death_increases_difficulty_when_kills_above_threshold(self):
        for _ in range(11):
            self.manager.on_wolf_killed()
        self.manager.on_player_died()
        self.assertEqual(self.manager.difficulty_multiplier, 1.2)

    def test_death_does_not_change_difficulty_when_kills_in_middle(self):
        for _ in range(5):
            self.manager.on_wolf_killed()
        self.manager.on_player_died()
        self.assertEqual(self.manager.difficulty_multiplier, 1.0)

    def test_difficulty_clamped_to_min(self):
        self.manager.difficulty_multiplier = 0.6
        for _ in range(2):
            self.manager.on_wolf_killed()
        self.manager.on_player_died()
        self.assertAlmostEqual(self.manager.difficulty_multiplier, DIFFICULTY_MIN)

    def test_difficulty_clamped_to_max(self):
        self.manager.difficulty_multiplier = 2.9
        for _ in range(11):
            self.manager.on_wolf_killed()
        self.manager.on_player_died()
        self.assertAlmostEqual(self.manager.difficulty_multiplier, DIFFICULTY_MAX)

    def test_reset_preserves_multiplier(self):
        self.manager.difficulty_multiplier = 1.5
        for _ in range(5):
            self.manager.on_wolf_killed()
        self.manager.reset_for_new_run()
        self.assertEqual(self.manager.difficulty_multiplier, 1.5)
        self.assertEqual(self.manager.wolves_killed_this_run, 0)

    def test_get_wolf_speed(self):
        speed = self.manager.get_wolf_speed()
        self.assertEqual(speed, WOLF_SPEED)

    def test_get_spawn_delay_bounds(self):
        for _ in range(100):
            delay = self.manager.get_spawn_delay()
            self.assertGreaterEqual(delay, WOLF_SPAWN_MIN_TIME)
            self.assertLessEqual(delay, WOLF_SPAWN_MAX_TIME)


if __name__ == "__main__":
    unittest.main()