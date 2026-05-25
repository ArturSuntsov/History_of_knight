import unittest

import pygame as pg

from core.geometry import apply_hitbox


class GeometryTests(unittest.TestCase):
  def test_apply_hitbox_shrinks_rect(self):
    base = pg.Rect(10, 20, 100, 80)
    result = apply_hitbox(base, 5, 20, 10, 30)
    self.assertEqual(result.x, 15)
    self.assertEqual(result.y, 30)
    self.assertEqual(result.width, 80)
    self.assertEqual(result.height, 50)


if __name__ == "__main__":
  unittest.main()
