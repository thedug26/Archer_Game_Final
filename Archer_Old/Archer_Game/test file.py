import pygame
from archconst import *
#Sets a game length
game_time=0
pygame.init()
#This class changes the poition of the players according to the level they are on
class Position():
    def __init__(self,x):
        self.x=x
        self.x1=(SCREEN_WIDTH/2)+TILE_SIZE
        self.time=pygame.time.get_ticks()
    def pos_update(self):
        if self.time>3:
            self.x+=TILE_SIZE-2*TILE_SIZE

ex=Position(100)
while True:
    print(ex.time)
print(ex.x)