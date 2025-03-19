# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GAME_TITLE = "Platformer Adventure"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Player settings
PLAYER_SPEED = 5
PLAYER_JUMP_POWER = -15
GRAVITY = 0.8

# Platform settings
PLATFORM_LIST = [
    (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),  # Ground
    (300, 400, 200, 20),                        # Platform 1
    (100, 300, 200, 20),                        # Platform 2
    (500, 200, 200, 20),                        # Platform 3
]

# Game states
MENU = "MENU"
PLAYING = "PLAYING"
GAME_OVER = "GAME_OVER"

# Coin settings
COIN_VALUE = 10
COIN_POSITIONS = [
    (350, 350),  # Above platform 1
    (150, 250),  # Above platform 2
    (550, 150),  # Above platform 3
]