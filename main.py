import pygame as pg
import os
from src.constants import *
from src.snake import Snake

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SNAKE GAME")

def main():
    clock = pg.time.Clock()
    snake = Snake()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                snake.change_direction(event.key)
        
        if snake.isGameover():
            running = False

        clock.tick(FPS)
        WIN.fill(BACKGROUND)
        snake.draw_snake(WIN)
        snake.move()
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()