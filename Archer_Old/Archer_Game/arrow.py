import pygame
import sys
import math
from archconst import *
# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("../Archer_Game/assets/Archer_Sprites/arrow.png")
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)
        self.speed += 0.01

        # Check if the projectile is out of the screen
        if self.rect.y > SCREEN_HEIGHT or self.rect.x < 0 or self.rect.x > SCREEN_WIDTH:
            self.kill()


