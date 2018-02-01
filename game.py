#!/usr/bin/python

import pygame, sys
#import launcher #create launcher file
from pygame.locals import *

pygame.init()

# color defs
DISPLAYSURF=pygame.display.set_mode((500,400),0,32)
SKY_COLOR=pygame.Color(62,131,247)
GRASS_GREEN=pygame.Color(48,96,41)
BLACK=(0,0,0)

ground=pygame.Rect(0,380,500,20) #makes ground

def draw_world(surf): #draws everything for scenery
    surf.fill(SKY_COLOR) #fills sky background
    pygame.draw.rect(surf,GRASS_GREEN,ground)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)  #font obj
    textSurfaceObj = fontObj.render('Launchr 1.0', True, BLACK, SKY_COLOR) #text obj
    textRectObj = textSurfaceObj.get_rect() #text box
    textRectObj.center = (250, 25) #text box center
    
    
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) #puts text to screen
    
    
    
while True: # main game loop
    draw_world(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                #launcher change, yada yada yada
                print "Up"
           # elif event.key==pygame.K_DOWN:
                ##...
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
   # my_launcher.draw(DISPLAYSURF)
    pygame.display.update()
  #  fpsClock.tick(FPS)
