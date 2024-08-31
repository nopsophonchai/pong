import pygame
from constant import *


class Shroom:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        # self.rect = pygame.Rect(x,y,66,79)
        self.rect = pygame.Rect(x,y,100,100)
        self.pic = pygame.image.load('./AJ_Pong/sprites/greyshroom.png')

    def render(self):
        
        # pygame.draw.rect(self.screen, (0,0,0,0), self.rect)
        self.screen.blit(self.pic, (self.x,self.y))

