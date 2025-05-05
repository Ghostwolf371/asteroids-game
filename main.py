import pygame
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()

    tm = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    Player.containers = updatable, drawable

    AsteroidField()
    Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = tm.tick(60) / 1000


if __name__ == "__main__":
    main()
