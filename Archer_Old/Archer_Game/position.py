import pygame, sys
from archconst import *
#Sets a game length
game_time=0
current_time=0
button_press_time=0

#This class changes the poition of the players according to the level they are on
class Position():
    def __init__(self,x):
        self.x=x
        self.x1=(SCREEN_WIDTH/2)+TILE_SIZE
        self.time=pygame.time.get_ticks()*1000
    #def pos_update(self,time):
    #    if time>3:
    #        self.x+=TILE_SIZE-2*TILE_SIZE





pygame.init()
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()


current_time=0
button_press_time=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            button_press_time=pygame.time.get_ticks()
            screen.fill((255,255,255))

    current_time=pygame.time.get_ticks()

    if current_time-button_press_time>2000:
        screen.fill((0,0,0))


    print(f"current_time: {current_time} button press time: {button_press_time}")
    pygame.display.flip()
    clock.tick(60)