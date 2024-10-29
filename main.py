# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display = pygame.display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        display.flip()


if __name__ == "__main__":
    main()
