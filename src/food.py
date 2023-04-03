import pygame as pg
import os
from src.constants import *

class Food():
    def __init__(self):
        self.food_image = pg.transform.scale(pg.image.load(os.path.join("assets", "food.png")), TILE)
        self.position = []