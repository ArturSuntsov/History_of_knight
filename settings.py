# Размеры экрана
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 416
FPS = 15

# Физика игрока
PLAYER_SPEED = 10
PLAYER_START_X = 150
PLAYER_START_Y = 230
PLAYER_MAX_X = 400 
JUMP_COUNT = 10
JUMP_THRESHOLD = -10
PLAYER_HEALTH = 3
PLAYER_ATTACK_COOLDOWN = 30
PLAYER_INVINCIBLE_DURATION = 30
PLAYER_BLINK_INTERVAL = 5

# Физика волка
WOLF_SPEED = 30
WOLF_SPAWN_X = 744
WOLF_SPAWN_Y = 280
WOLF_SPAWN_MIN_TIME = 1000
WOLF_SPAWN_MAX_TIME = 2000
WOLF_SPAWN_INITIAL_MIN = 3000
WOLF_SPAWN_INITIAL_MAX = 4000
WOLF_DESPAWN_X = -100

# Цвета
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (65, 65, 65)

# Пути к ресурсам
ICON_PATH = "assets/images/knight.png"
HEART_PATH = "assets/images/heart.png"
WOLF_FACE_PATH = "assets/images/wolf_face.png"
BG_PATH = "assets/images/back.png"
BG_MUSIC_PATH = "assets/sounds/journey.mp3"
FONT_PATH = "assets/fonts/ofont.ru_Mephisto.ttf"
FONT_SIZE = 70

# Позиции UI элементов
HEART_START_X = 10
HEART_START_Y = 10
HEART_SPACING = 40
WOLF_ICON_X = 10
WOLF_ICON_Y = 70
SCORE_TEXT_X = 70
SCORE_TEXT_Y = 70

# Game Over экран
GAME_OVER_TEXT_X = 150
GAME_OVER_TEXT_Y = 70
RESTART_BUTTON_X = 150
RESTART_BUTTON_Y = 230
SCORE_KILLS_X = 150
SCORE_KILLS_Y = 150

# Размеры спрайтов 
PLAYER_SPRITE_WIDTH = 184
PLAYER_SPRITE_HEIGHT = 160
WOLF_SPRITE_WIDTH = 130
WOLF_SPRITE_HEIGHT = 65

# Hitbox для игрока
PLAYER_HITBOX_X_OFFSET = 58
PLAYER_HITBOX_WIDTH_REDUCE = 120
PLAYER_HITBOX_Y_OFFSET = 53
PLAYER_HITBOX_HEIGHT_REDUCE = 107

# Hitbox для волка
WOLF_HITBOX_X_OFFSET = 25
WOLF_HITBOX_WIDTH_REDUCE = 50
WOLF_HITBOX_Y_OFFSET = 25
WOLF_HITBOX_HEIGHT_REDUCE = 25

# Анимации
PLAYER_RIGHT_PATHS = [f"assets/images/Player/player_right/run ({i}).png" for i in range(1, 9)]
PLAYER_LEFT_PATHS = [f"assets/images/Player/player_left/run ({i}).png" for i in range(1, 9)]
WOLF_RUN_PATHS = [f"assets/images/wolf/run/wolf ({i}).png" for i in [3, 2, 5, 1, 4, 6]]
WOLF_ATTACK_PATHS = [f"assets/images/wolf/attack/wolf ({i}).png" for i in range(7, 12)]
PLAYER_ATTACK_PATHS = [f"assets/images/Player/player_attack/attack ({i}).png" for i in range(1, 7)]

# Фон
BG_SCROLL_SPEED = 3
