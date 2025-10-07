import pygame
import random
from circleshape import *
from constants import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius)

    def update(self,dt):
        self.position += dt * self.velocity

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            asteroid1_velocity, asteroid2_velocity = self.velocity.rotate(angle),self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid1.velocity = 1.2 * asteroid1_velocity
            asteroid2.velocity = 1.2 * asteroid2_velocity
        self.kill()