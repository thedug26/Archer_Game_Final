import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ballistic Projectiles with Angles and Gravity in Pygame")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)
        self.speed += gravity

        # Check if the projectile is out of the screen
        if self.rect.y > height or self.rect.x < 0 or self.rect.x > width:
            self.kill()


# Cannon class
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 30)

# Gravity
gravity = 0.01

# Sprite groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Create cannon
cannon = Cannon()
all_sprites.add(cannon)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a projectile when the spacebar is pressed
                angle = 45  # Initial launch angle
                projectile = Projectile(cannon.rect.centerx, cannon.rect.centery, angle)
                all_sprites.add(projectile)
                projectiles.add(projectile)

    all_sprites.update()

    # Draw everything
    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)


