import pygame as pg

WIDTH, HEIGHT = 800, 800
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SNAKE GAME")

def main():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    pg.quit()

if __name__ == "__main__":
    main()