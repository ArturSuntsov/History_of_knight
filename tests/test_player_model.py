import unittest

import pygame as pg

from player.model import PlayerModel
from settings import (
    JUMP_COUNT,
    PLAYER_HEALTH,
    PLAYER_INVINCIBLE_DURATION,
    PLAYER_MAX_X,
    PLAYER_SPEED,
    PLAYER_START_X,
)


class FakeKeys:
  def __init__(self, pressed=None):
    self._pressed = pressed or set()

  def __getitem__(self, key):
    return key in self._pressed


class PlayerModelTests(unittest.TestCase):
  def setUp(self):
    self.player = PlayerModel()

  def test_attack_starts_only_without_cooldown(self):
    self.player.attack_cooldown = 5
    self.player.attack()
    self.assertFalse(self.player.is_attacking)

    self.player.attack_cooldown = 0
    self.player.attack()
    self.assertTrue(self.player.is_attacking)

  def test_take_damage_respects_invincibility(self):
    self.player.take_damage()
    self.assertEqual(self.player.health, PLAYER_HEALTH - 1)
    self.assertEqual(self.player.invincible_timer, PLAYER_INVINCIBLE_DURATION)

    self.player.take_damage()
    self.assertEqual(self.player.health, PLAYER_HEALTH - 1)

  def test_movement_respects_bounds(self):
    self.player.x = 0
    self.player.update(FakeKeys({pg.K_LEFT}))
    self.assertEqual(self.player.x, 0)

    self.player.x = PLAYER_MAX_X
    self.player.update(FakeKeys({pg.K_RIGHT}))
    self.assertEqual(self.player.x, PLAYER_MAX_X)

  def test_movement_changes_position(self):
    self.player.update(FakeKeys({pg.K_RIGHT}))
    self.assertEqual(self.player.x, PLAYER_START_X + PLAYER_SPEED)

  def test_reset_restores_defaults(self):
    self.player.health = 0
    self.player.x = 999
    self.player.reset()
    self.assertEqual(self.player.health, PLAYER_HEALTH)
    self.assertEqual(self.player.x, PLAYER_START_X)
    self.assertEqual(self.player.jump_count, JUMP_COUNT)


if __name__ == "__main__":
  unittest.main()
