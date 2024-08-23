import pygame
from constant import *

class Paddle:
    def __init__(self,screen, x,y ,width, height):
        self.screen = screen
        self.rect = pygame.Rect(x,y,width,height)
        self.dy = 0


    def update(self,dt):
        if self.dy >0:
            if self.rect.y + self.rect.height < height:
                self.rect.y += self.dy * dt
        else:
            if self.rect.y >= 0:
                self.rect.y += self.dy*dt


        # if not (self.rect.x > (ball.rect.x + ball.rect.width)) and not ((self.rect.x + self.rect.width) < ball.rect.x) and not (self.rect.y > (ball.rect.y + ball.rect.height)) and not ((self.rect.y + self.rect.height) < ball.rect.y):

    def render(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)