from numpy import cos, sin
import pygame
from colors import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

class Launcher:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = 100
        self.angle = -45
        # the launcher is located at (x,y)
        # with the initial state:
        # magnitude = 20
        # angle = 45 deg

    def changeMagnitude(self, delta):
        if self.magnitude <= MAX_MAG and self.magnitude >= MIN_MAG:
            self.magnitude += delta
            # adjust the magnitude
            # within MIN / MAX bounds

    def changeAngle(self, delta):
        if self.angle <= MAX_ANGLE and self.angle >= MIN_ANGLE:
            self.angle += delta
            # adjust the angle
            # within MIN / MAX bounds
    
    def draw(self, surf):
        pygame.draw.line(surf,BROWN,(self.x,self.y),((self.x + self.magnitude *cos(self.angle*3.14/180.0)), (self.y + self.magnitude * sin(self.angle*3.14/180.0))), 4)
