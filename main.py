import pygame as pg
from src.constants import *
from src.snake import Snake
from src.food import Food

pg.display.set_caption("SNAKE GAME")

def main():
    clock = pg.time.Clock()
    snake = Snake()
    food = Food()
    food.set_position(snake)
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                snake.change_direction(event.key)
        
        if snake.isGameover():
            running = False
        
        if snake.sections[0] == food.position:
            snake.eat()
            food.set_position(snake)

        clock.tick(FPS)
        WIN.fill(BACKGROUND)
        snake.draw_snake(WIN)
        food.draw_food(WIN)
        snake.move()
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()