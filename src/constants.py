from pygame import display

# Proportions
WIDTH, HEIGHT = 800, 800
TILE = (32, 32)
WIDTH_TILES = WIDTH // TILE[0]
HEIGHT_TILES = HEIGHT // TILE[1]
WIN = display.set_mode((WIDTH, HEIGHT))

# Game time
FPS = 5

# Movement Directions
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

# Colors
BACKGROUND = (0, 0, 0)