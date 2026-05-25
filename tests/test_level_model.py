import unittest

from level.model import LevelModel
from settings import BG_SCROLL_SPEED, SCREEN_WIDTH


class LevelModelTests(unittest.TestCase):
    def setUp(self):
        self.level = LevelModel()

    def test_background_scrolls_left(self):
        self.level.update()
        self.assertEqual(self.level.bg_x, -BG_SCROLL_SPEED)

    def test_background_wraps_after_one_screen(self):
        self.level.bg_x = -SCREEN_WIDTH
        self.level.update()
        self.assertEqual(self.level.bg_x, 0)

    def test_reset_returns_to_start(self):
        self.level.bg_x = -200
        self.level.reset()
        self.assertEqual(self.level.bg_x, 0)


if __name__ == "__main__":
  unittest.main()
