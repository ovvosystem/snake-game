import pygame as pg
import os
from src.constants import *

class Snake():
    def __init__(self):
        self.head = pg.image.load(os.path.join("assets", "snake_head.png"))
        self.head = pg.transform.scale(self.head, constants.TILE)
        self.body = pg.image.load(os.path.join("assets", "snake_body.png"))
        self.body = pg.transform.scale(self.body, constants.TILE)
        self.sections = [[WIDTH_TILES // 2, HEIGHT_TILES // 2],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 1],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 2]]
        self.direction = UP