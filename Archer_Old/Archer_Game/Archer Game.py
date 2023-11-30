import sys

import pygame

from backarcher import *
from archer_player import *
from arrow import Projectile
import math

#from position import Position

#initialize game
pygame.init()

#background
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Archer Game Beta')
clock=pygame.time.Clock()

#score counter
score=0

#contact noise
#hit=pygame.mixer.Sound("../assets/sounds/scream.wav")

current_time=0
button_press_time=0

# Sprite groups
sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

custom_font = pygame.font.Font("../Archer_Game/assets/fonts/Kenney Future.ttf", 48)

text = custom_font.render("Archer", True, (255, 0, 0))




running=True
background=screen.copy()
draw_background(background)

soldier = Player(player1x, SCREEN_HEIGHT - TILE_SIZE * 5 -5)
#print(soldier.rect.width, soldier.rect.height)
adventurer = Player(player2x, SCREEN_HEIGHT - TILE_SIZE * 5 -5)

#sprites.add(soldier)
sprites.add(projectiles)
#sprites.add(adventurer)
#soldier_shoot=Bullet(soldier.self.x,soldier.self.y)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #running=False
            pygame.quit()
            sys.exit()
        #if event.type == pygame.MOUSEBUTTONUP:
        #    button_press_time = pygame.time.get_ticks()
        #    soldier.pos_update(current_time)
        #    adventurer.pos_update1(current_time)
            #soldier.draw(screen)
            #print("click")

        #shoots an arrow using spacebar
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a projectile when the spacebar is pressed
                angle = 0  # Initial launch angle
                projectile = Projectile(soldier.rect.centerx, soldier.rect.centery, angle)


                sprites.add(projectile)

        #result = pygame.sprite.spritecollide(sprites[0], sprites[1], False)


        #if result:
        #    pygame.mixer.Sound.play(hit)
            #score += len(result)
            #print(score)

            #projectiles.add(projectile)
            #print('space')




        current_time = pygame.time.get_ticks()


    screen.blit(background, (0, 0))

    #draw sprites

    soldier.draw(screen)
    adventurer.draw2(screen)

    #screen.blit(background, (0, 0))

    soldier.update()
    adventurer.update()

    sprites.update()
    sprites.draw(screen)
    #projectiles.draw(screen)


    #text = score_font.render(f'{score}', True, (255, 0, 0))

    #screen.blit(text,(SCREEN_WIDTH-TILE_SIZE,0))

    pygame.display.flip()
    clock.tick(30)


#pygame.quit()
#sys.exit()



#timing info

