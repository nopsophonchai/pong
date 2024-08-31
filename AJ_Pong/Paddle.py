import pygame
from constant import *

class Paddle:
    def __init__(self, screen, x, y, width, height, speed,player):
        self.screen = screen
        self.height = height
        self.width = width
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.dy = speed
        self.defaultDy = speed
        self.defaultHeight = height
        if player == 1:
            self.defaultPic = pygame.image.load('/Users/noppynorthside/Desktop/GameDev/AJ_Pong/sprites/player1.png')
            self.bigPic = pygame.image.load('/Users/noppynorthside/Desktop/GameDev/AJ_Pong/sprites/player1big.png')
        elif player == 2:
            self.defaultPic = pygame.image.load('/Users/noppynorthside/Desktop/GameDev/AJ_Pong/sprites/player2.png')
            self.bigPic = pygame.image.load('/Users/noppynorthside/Desktop/GameDev/AJ_Pong/sprites/player2big.png')

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
        if self.rect.height == 100:
            self.screen.blit(self.defaultPic, (self.rect.x,self.rect.y))
        if self.rect.height == 150:
            self.screen.blit(self.bigPic, (self.rect.x,self.rect.y))
        