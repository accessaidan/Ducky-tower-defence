import pygame as pg
from enemies import Enemy
import constants as c
import os
pg.init()

#create clock
clock = pg.time.Clock()


#making screen
screen = pg.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
pg.display.set_caption("Tower defence")

#load images
enemy_image = pg.image.load('C:\\Users\Aidan Hedges\\Documents\\coding\\games\\Ducky-tower-defence\\assets\\images\\enemies\\enemy_1.png').convert_alpha()

#create group
enemy_group = pg.sprite.Group()


enemy = Enemy((200,300), enemy_image)
enemy_group.add(enemy)


#game loop
run = True
while run:

    clock.tick(c.FPS)
    
    #event handler
    for event in pg.event.get():
      
        #quit program
        if event.type == pg.QUIT:
            run = False

pg.quit()