import pygame
from constant import *

class Paddle:
    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.height = height
        self.width = width
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.dy = speed
        self.defaultDy = speed
        self.defaultHeight = height

    def update(self, dt):
        if self.dy > 0:
            if self.rect.y + self.rect.height < HEIGHT:
                self.rect.y += self.dy*dt
        else:
            if self.rect.y >= 0:
                self.rect.y += self.dy*dt
    def reset(self):
        self.dy = self.defaultDy
        self.rect.height = self.defaultHeight

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)