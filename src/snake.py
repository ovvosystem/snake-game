import pygame as pg
import os
from src.constants import *

class Snake():
    def __init__(self):
        # Load snake assets
        self.head_image = pg.transform.scale(pg.image.load(os.path.join("assets", "snake_head.png")), TILE)
        self.head = self.head_image
        self.body_image = pg.transform.scale(pg.image.load(os.path.join("assets", "snake_body.png")), TILE)
        self.body = self.body_image
        # Sections that compose the snake
        self.sections = [[WIDTH_TILES // 2, HEIGHT_TILES // 2],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 1],
                         [WIDTH_TILES // 2, HEIGHT_TILES // 2 + 2]]
        self.direction = UP
        self.new_direction = UP
    
    def change_direction(self, key):
        # Change direction if not moving on opposite direction
        if key == pg.K_UP and self.direction != DOWN:
            self.new_direction = UP
            self.head = pg.transform.rotate(self.head_image, 0)
        if key == pg.K_DOWN and self.direction != UP:
            self.new_direction = DOWN
            self.head = pg.transform.rotate(self.head_image, 180)
        if key == pg.K_LEFT and self.direction != RIGHT:
            self.new_direction = LEFT
            self.head = pg.transform.rotate(self.head_image, 90)
        if key == pg.K_RIGHT and self.direction != LEFT:
            self.new_direction = RIGHT
            self.head = pg.transform.rotate(self.head_image, 270)

    def move(self):
        # Move snake in current direction
        self.direction = self.new_direction
        self.sections.insert(0, [self.sections[0][0] + self.direction[0],
                                 self.sections[0][1] + self.direction[1]])
        self.sections.pop(-1)

    def draw_snake(self, window):
        # Draw snake in window
        window.blit(self.head, (self.sections[0][0] * TILE[0], self.sections[0][1] * TILE[1]))
        for section in self.sections[1:]:
            window.blit(self.body, (section[0] * TILE[0], section[1] * TILE[1]))

    def eat(self):
        # Grow snake another section
        self.sections.append(self.sections[-1])

    def isGameover(self):
        # Check for game over conditions

        # Check if snake hit window border
        def hit_wall():
            if self.sections[0][0] < 0 or self.sections[0][0] >= WIDTH_TILES:
                return True
            elif self.sections[0][1] < 0 or self.sections[0][1] >= HEIGHT_TILES:
                return True
            else:
                return False
        
        # Check if snake hit itself
        def hit_self():
            for section in self.sections[1:]:
                if self.sections[0] == section:
                    return True
            return False
        
        return hit_wall() or hit_self()