import pygame, sys

class Players(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

    def update(self):
        self.rect.center=pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        #self.image=pygame.Surface((50,10))
        #draws arrow to shoot
        self.image=pygame.image.load("../assets/Archer_Sprites/arrow.png")

        #not needed for image
        #self.image.fill((255,0,0))
        #tells bullet its position
        self.rect=self.image.get_rect(center=(pos_x,pos_y))

    def update(self):
        self.rect.x+=5

        if self.rect.x>=SCREEN_WIDTH+200:
            self.kill()


pygame.init()
clock=pygame.time.Clock()
SCREEN_WIDTH,SCREEN_HEIGHT=800,800
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.mouse.set_visible(False)

player=Players()
player_group=pygame.sprite.Group()
player_group.add(player)

bullet_group=pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    #drawing
    screen.fill((30,30,30))

    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pygame.display.flip()
    clock.tick(120)