import unittest

from settings import WOLF_DESPAWN_X, WOLF_SPEED, WOLF_SPAWN_X
from wolf.model import WolfModel


class WolfModelTests(unittest.TestCase):
    def setUp(self):
        self.wolf = WolfModel()  
    
    def test_moves_left_each_update(self):
        self.wolf.update() 
        self.assertEqual(self.wolf.x, WOLF_SPAWN_X - WOLF_SPEED)
    
    def test_should_despawn_off_screen(self):
        self.wolf.x = WOLF_DESPAWN_X - 1
        self.assertTrue(self.wolf.should_despawn())
        
        self.wolf.x = WOLF_DESPAWN_X
        self.assertFalse(self.wolf.should_despawn())
    
    def test_get_rect_is_smaller_than_sprite(self):
        rect = self.wolf.get_rect()
        self.assertLess(rect.width, 130)
        self.assertLess(rect.height, 65)


if __name__ == "__main__":
  unittest.main()
