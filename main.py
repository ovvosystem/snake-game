import pygame as pg
from src.constants import *
from src.snake import Snake
from src.food import Food

pg.display.set_caption("SNAKE GAME")

def main():
    # Prepare game objects
    clock = pg.time.Clock()
    snake = Snake()
    food = Food()

    # Set initial food position
    food.set_position(snake)

    # Run the game
    running = True

    while running:
        for event in pg.event.get():
            # Quit game
            if event.type == pg.QUIT:
                running = False

            # Change direction on key input
            elif event.type == pg.KEYDOWN:
                snake.change_direction(event.key)
        
        # Eat food if snake's head touches it
        if snake.sections[0] == food.position:
            snake.eat()
            food.set_position(snake)

        # Prepare new frame
        snake.move()
        WIN.fill(BACKGROUND)
        snake.draw_snake(WIN)
        food.draw_food(WIN)

        # Tick FPS
        clock.tick(FPS)

        # Load new frame
        pg.display.update()

        # Check for game over conditions
        if snake.isGameover():
            running = False

    pg.quit()

if __name__ == "__main__":
    main()