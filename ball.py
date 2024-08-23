import pygame
from constant import *
import random

class Ball:
    def __init__(self, screen, x ,y, width, height):
        self.screen = screen

        self.rect = pygame.Rect(x,y,width,height)

        self.dx = random.choice([-300,300])
        self.dy = random.randint(-150,150)

    def reset(self):
        self.rect.x = width/2 -6
        self.rect.y = height/2 -6
        self.dx = random.choice([-300,300])
        self.dy = random.randint(-150,150)

    def collsion(self):
        self.dx = -self.dx
        self.dy = -self.dy


    def update(self,dt):
        self.rect.x += self.dx*dt
        self.rect.y += self.dy*dt
    
    def render(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)