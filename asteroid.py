import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2) # position is a Vector2

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        r_angle = random.uniform(20,50)
        v_plus = self.velocity.rotate(r_angle)
        v_minus = self.velocity.rotate(-r_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1, new_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius), Asteroid(self.position.x,self.position.y, new_radius)
        new_asteroid1.velocity = 1.2 * v_plus
        new_asteroid2.velocity = 1.2 * v_minus
