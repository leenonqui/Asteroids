# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():

    # setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # update updatable items
        for item in updatable:
            item.update(dt)

        # draw drawable items
        for item in drawable:
            item.draw(screen)

        # chacks for collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                pygame.quit()
                print("Game Over!")
                return

        # refreshes
        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = clock.tick(FPS) #60fps / 1000



if __name__ == "__main__":
    main()
