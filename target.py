import pygame, sys
from colors import *
import numpy

class Target:
    def __init__(self):
        self.topLX=numpy.random.randint(100,320)
        self.topLY=379
        self.width=40
        self.height=10
        self.target=pygame.Rect(self.topLX,self.topLY,self.width,self.height)

    def draw(self,surf):
        pygame.draw.rect(surf,BLACK,self.target)
    
    def hitBy(self,obj):
        return self.target.colliderect(obj.getRect())
