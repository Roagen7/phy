import math
import pygame
import time

from src.classes.Ball import Ball
from src.classes.Force import Force
from src.classes.Area import Area
from src.classes.Center import Center

from src.methods.run_collisions import run_collisions

# ^  -y
#/ \
# | 
# |
# |     x
# ------ >
#       
 



#variables

pygame.init()

InfoObject = pygame.display.Info()

width = int(InfoObject.current_w)
height = int(InfoObject.current_h)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("zderzenia.py")
FPS = 30
borders = 10
energy_loss = 1

area1 = Area(width/2, 0, width/2, height, [Force("x", 5), Force("y",-15)], (125,0,0))
area2 = Area(100, 100, 200, 200, [Force("y", -30)], (0,0,125))
areaGravity= Area(0, 0, width, height, [Force("y", 10)], (0,0,0))
area3 = Area(0, 0, width, height, [], (0,0,0))
 

ballx = Ball(0,0,10,20, (250,0,0), FPS)
ballx.vx = 10
ballx.vy = 10 
bally = Ball(450,450, 10, 20, (0,250,0), FPS)
bally.vx =  10
bally.vy = 10

cent1 = Center(500, 500, 10, 5, (150,150,150), Force("x", 1), Force("y",1)) 
cent2 = Center(750, 500, 10, 5, (150,0,150), Force("x", 1), Force("y",1)) 
balls = [bally,ballx]
areas = [area3, area2, area1 ]
centers = [cent1, cent2]
bally.angle = 0

balls = [bally]
areas = []
centers = []

#for ball in balls:
#    ball.apply_force(Force("y",ball.m * 10))




run = True

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    gameDisplay.fill((0,0,0))
    #pygame.draw.rect(gameDisplay,(0,0,125),[width/2, 0, width/2, height],0)
    for area in areas:
        area.draw(pygame, gameDisplay)
    for center in centers:
        center.draw(pygame, gameDisplay)

    for ball in balls:
        ball.move()
        ball.draw(pygame, gameDisplay)

    run_collisions(balls,areas,centers,borders,width,height, energy_loss)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

