import unittest

import pygame as pg

from core.game_state import GameState
from player.model import PlayerModel
from settings import PLAYER_HEALTH, WOLF_SPAWN_X, WOLF_SPAWN_Y
from wolf.model import WolfModel


class GameStateTests(unittest.TestCase):
  def setUp(self):
    self.state = GameState()

  def test_add_wolf_increases_list(self):
    self.state.add_wolf()
    self.assertEqual(len(self.state.wolves), 1)

  def test_attack_kills_overlapping_wolf(self):
    self.state.player.is_attacking = True
    wolf = WolfModel()
    wolf.x = self.state.player.x
    wolf.y = self.state.player.y
    self.state.wolves.append(wolf)

    self.state.update_wolves()
    self.assertEqual(self.state.wolves_killed, 1)
    self.assertEqual(len(self.state.wolves), 0)

  def test_collision_damages_player(self):
    wolf = WolfModel()
    wolf.x = self.state.player.x
    wolf.y = self.state.player.y
    self.state.wolves.append(wolf)

    self.state.update_wolves()
    self.assertEqual(self.state.player.health, PLAYER_HEALTH - 1)
    self.assertTrue(wolf.attacking)

  def test_reset_clears_progress(self):
    self.state.wolves_killed = 5
    self.state.wolves.append(WolfModel())
    self.state.gameplay = False

    self.state.reset()
    self.assertEqual(self.state.wolves_killed, 0)
    self.assertEqual(len(self.state.wolves), 0)
    self.assertTrue(self.state.gameplay)


if __name__ == "__main__":
  unittest.main()
