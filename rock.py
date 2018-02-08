import pygame
from colors import *

G = 25

class Rock:
    def  __init__(self,x,y):
        #TODO figure out what to do here
        self.x=x
        self.y=y
        self.v_x=0
        self.v_y=0
        self.r=(0,0,0,0)

    def move(self,time):
        #move in x
        self.x=self.x+self.v_x*time
        #move in y
        if(self.v_y!=0):        
            self.v_y+=G*time
        self.y+=self.v_y*time
        
    def draw(self,surf):
        self.r = pygame.Rect((0,0,10,10))
        self.r.center = (self.x, self.y)
        pygame.draw.rect(surf, GREY, self.r)
    
    def isMoving(self):
        return (self.v_x!=0 or self.v_y!=0)

    def moveTo(self,x,y):
        self.x=x
        self.y=y
        self.v_x=0
        self.v_y=0

    def getRect(self):
        return self.r
