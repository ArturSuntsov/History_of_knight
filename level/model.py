from settings import BG_SCROLL_SPEED, SCREEN_WIDTH


class LevelModel:
    """Позиция прокручиваемого фона."""

    def __init__(self):
        self.bg_x = 0

    def update(self):
        self.bg_x -= BG_SCROLL_SPEED
        if self.bg_x <= -SCREEN_WIDTH:
            self.bg_x = 0

    def reset(self):
        self.bg_x = 0
