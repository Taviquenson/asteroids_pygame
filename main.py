# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # delta time: used to represent the amount of time that has passed since the last frame was drawn

    # declare groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the static "container" field of the sprite classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # IMPORTANT: Instances of sprites like "player" MUST be created after their clases are added to the groups/containers like in previous line
    # NOTICE that even though object "player" gets marked as an unused
    # variable, it is being used trough the call done on the containers 
    # instantiate a Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    



    while True:
        time_since_last_tick = clock.tick(60) # pauses the game loop until 1/60th of a second has passed.
        # also returns the amount of time that has passed since the last time it was called: the delta time
        dt = time_since_last_tick / 1000 # divide by 1,000 to convert from milliseconds to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # No need to iterate "updatable" container because the pygame library knows how to handle this efficiently
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split() 
                    # kill() removes the object from all of its groups
                    shot.kill()

        # With a "draw" function, you need to tell Pygame where to draw each sprite, and thus you need to iterate "drawable"
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # display updates


if __name__ == "__main__":
    main()
