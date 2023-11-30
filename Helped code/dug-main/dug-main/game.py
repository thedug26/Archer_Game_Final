import pygame
from adventurer import Adventurer
from target import Target

# Set the width and height of the game window
WIDTH = 1200
HEIGHT = 600

# create clock
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# make arrows group
arrows = pygame.sprite.Group()

# Create an adventurer at center of the screen
my_adventurer = Adventurer(WIDTH//2, HEIGHT - 100, arrows, screen)

# Create a target
my_target = Target(WIDTH//2 + 200, HEIGHT - 100, screen)

# Set the running flag to True
running = True

# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
        # If the user closes the window, set running to False
        if event.type == pygame.QUIT:
            running = False

    # Set the game's FPS
    clock.tick(60)

    screen.fill('black')

    # Update the adventurer & arrows
    my_adventurer.update()
    arrows.update()

    # Draw the adventurer, arrows, & target
    [b.draw(my_target, screen) for b in arrows]
    my_adventurer.draw()
    my_target.draw()

    # Update the display
    pygame.display.flip()

pygame.quit()
