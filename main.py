# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # delta time: used to represent the amount of time that has passed since the last frame was drawn

    # instantiate a Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        time_since_last_tick = clock.tick(60) # pauses the game loop until 1/60th of a second has passed.
        # also returns the amount of time that has passed since the last time it was called: the delta time
        dt = time_since_last_tick / 1000 # divide by 1,000 to convert from milliseconds to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip() # display updates


if __name__ == "__main__":
    main()
