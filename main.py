import pygame as pg
import os
from src.constants import *

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SNAKE GAME")

# Assets
BACKGROUND = (0, 0, 0)
SNAKE_BODY_IMAGE = pg.image.load(os.path.join('assets', 'snake_body.png'))
SNAKE_BODY = pg.transform.scale(SNAKE_BODY_IMAGE, TILE)
SNAKE_HEAD_IMAGE = pg.image.load(os.path.join('assets', 'snake_head.png'))
SNAKE_HEAD = pg.transform.scale(SNAKE_HEAD_IMAGE, TILE)

def main():
    clock = pg.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        draw_window()

    pg.quit()

def draw_window():
    WIN.fill(BACKGROUND)
    WIN.blit(SNAKE_BODY, ((WIDTH/2) - 16, (HEIGHT/2) - 16))
    pg.display.update()

if __name__ == "__main__":
    main()