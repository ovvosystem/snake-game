import pygame as pg
import os
from random import randrange
from src.constants import *

class Food():
    def __init__(self):
        self.food_image = pg.transform.scale(pg.image.load(os.path.join("assets", "food.png")), TILE)
        self.position = []
    
    def set_position(self, snake):
        # Set food's position on the screen
        self.position = [randrange(0, WIDTH_TILES - 1), randrange(0, HEIGHT_TILES - 1)]
        while self.position in snake.sections:
            self.position = [randrange(0, WIDTH_TILES - 1), randrange(0, HEIGHT_TILES - 1)]

    def draw_food(self, window):
        # Draw food in window
        window.blit(self.food_image, (self.position[0] * TILE[0], self.position[1] * TILE[1]))