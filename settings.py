SCREEN_WIDTH = 740
SCREEN_HEIGHT = 416
FPS = 15
PLAYER_SPEED = 6
WOLF_SPEED = 20
JUMP_COUNT = 10

WHITE = [255, 255, 255]
GRAY = [128, 128, 128]
BLUE = [0, 0, 255]

ICON_PATH = "assets/images/knight.png"
BG_PATH = "assets/images/back.png"
BG_MUSIC_PATH = "assets/sounds/journey.mp3"
FONT_PATH = "assets/fonts/ofont.ru_Mephisto.ttf"
FONT_SIZE = 70

PLAYER_RIGHT_PATHS = (f"assets/images/Player/player_right/run ({i}).png" for i in range(1, 9))

PLAYER_LEFT_PATHS = (f"assets/images/Player/player_left/run ({i}).png" for i in range(1, 9))

WOLF_RUN_PATHS = (f"assets/images/wolf/run/wolf ({i}).png" for i in [3, 2, 5, 1, 4, 6])

WOLF_ATTACK_PATHS = (f"assets/images/wolf/attack/wolf ({i}).png" for i in range(7, 12))
