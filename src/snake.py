import pygame as pg
import os
from src.constants import *

class Snake():
    def __init__(self):
        # Load snake assets
        self.head = pg.image.load(os.path.join("assets", "snake_head.png"))
        self.head = pg.transform.scale(self.head, TILE)
        self.body = pg.image.load(os.path.join("assets", "snake_body.png"))
        self.body = pg.transform.scale(self.body, TILE)
        # Sections that compose the snake
        self.sections = [[WIDTH_TILES // 2, HEIGHT_TILES // 2],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 1],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 2]]
        self.direction = UP
    
    def change_direction(self, key):
        # Change direction if not moving on opposite direction
        if key == pg.K_UP and self.direction != DOWN:
            self.direction = UP
        if key == pg.K_DOWN and self.direction != UP:
            self.direction = DOWN
        if key == pg.K_LEFT and self.direction != RIGHT:
            self.direction = LEFT
        if key == pg.K_RIGHT and self.direction != LEFT:
            self.direction = RIGHT

    def move(self):
        # Move snake in current direction
        self.sections.insert(0, [self.sections[0][0] + self.direction[0],
                                 self.sections[0][1] + self.direction[1]])
        self.sections.pop(-1)

    def draw_snake(self, window):
        # Draw snake in window
        window.blit(self.head, (self.sections[0][0] * TILE[0], self.sections[0][1] * TILE[1]))
        for section in self.sections[1:]:
            window.blit(self.body, (section[0] * TILE[0], section[1] * TILE[1]))