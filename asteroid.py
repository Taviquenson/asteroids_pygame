import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() # always remove the asteroid that was shot
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # a small asteroid was shot so we are done
        
        # create the direcions for the new smaller asteroids
        angle = random.uniform(20, 50)
        vector_pos = self.velocity.rotate(angle)
        vector_neg = self.velocity.rotate(-angle)

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        pos_angle_ast = Asteroid(self.position.x, self.position.y, smaller_radius)
        neg_angle_ast = Asteroid(self.position.x, self.position.y, smaller_radius)

        pos_angle_ast.velocity = vector_pos * 1.2
        neg_angle_ast.velocity = vector_neg * 1.2