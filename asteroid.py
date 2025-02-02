from CircleShape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, ASTEROID_LINE_THICKNESS)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a_1 = Asteroid(*self.position, new_radius)
            a_1.velocity = self.velocity.rotate(-new_radius) * 1.2
            a_2 = Asteroid(*self.position, new_radius)
            a_2.velocity = self.velocity.rotate(new_radius) * 1.2


    def update(self, dt):
        self.position  += dt * self.velocity

