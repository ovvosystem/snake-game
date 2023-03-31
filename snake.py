import pygame as pg
import os

WIDTH, HEIGHT = 800, 800
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pg.display.set_caption("SNAKE GAME")

BACKGROUND = (0, 0, 0)
SNAKE_BODY_IMAGE = pg.image.load(os.path.join('assets', 'snake_body.png'))
SNAKE_BODY = pg.transform.scale(SNAKE_BODY_IMAGE, (32, 32))

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