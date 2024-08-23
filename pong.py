import pygame
import sys
import random
from ball import Ball
from paddle import Paddle
from constant import *




class GameMain:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((width,height))
        self.small_font = pygame.font.Font("./font.ttf", 24)
        self.medium_font = pygame.font.Font("./font.ttf",48)
        self.large_font = pygame.font.Font("./font.ttf",72)

        self.player1 = Paddle(self.screen, 30,90,15,60)
        self.player2 = Paddle(self.screen,width-30,90,15,60)
        self.ball = Ball(self.screen,width/2-6,height/2-6,12,12)
        self.game_state = 'start'

    def update(self, dt, events):
        #dt = how much real time has passed
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_state == 'start':
                        self.game_state = 'play'
                    else:
                        self.game_state = 'start'
                        self.ball.reset()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player1.dy = -paddleSpeed
        elif key[pygame.K_s]:
            self.player1.dy = paddleSpeed
        else:
            self.player1.dy = 0

        if key[pygame.K_UP]:
            self.player2.dy = -paddleSpeed
        elif key[pygame.K_DOWN]:
            self.player2.dy = paddleSpeed
        else:
            self.player2.dy = 0

        if self.game_state == 'play':
            self.ball.update(dt)
        
        if not (self.player1.rect.x > (self.ball.rect.x + self.ball.rect.width)) and not ((self.player1.rect.x + self.player1.rect.width) < self.ball.rect.x) and not (self.player1.rect.y > (self.ball.rect.y + self.ball.rect.height)) and not ((self.player1.rect.y + self.player1.rect.height) < self.ball.rect.y):
            self.ball.collsion()
        if not (self.player2.rect.x > (self.ball.rect.x + self.ball.rect.width)) and not ((self.player2.rect.x + self.player2.rect.width) < self.ball.rect.x) and not (self.player2.rect.y > (self.ball.rect.y + self.ball.rect.height)) and not ((self.player2.rect.y + self.player2.rect.height) < self.ball.rect.y):
            self.ball.collsion()
        self.player1.update(dt)
        self.player2.update(dt)


    def render(self):
        self.screen.fill((40,45,52))
        t_welcome = self.small_font.render("welcome pong", False, (225,255,255))
        text_rect = t_welcome.get_rect(center=(width/2,60))
        self.screen.blit(t_welcome,text_rect)

        self.ball.render()
        self.player1.render()
        self.player2.render()

if __name__ == '__main__':
    main = GameMain()
    clock = pygame.time.Clock()

    while True:
        pygame.display.set_caption("Pong game running with {:d} FPS".format(int(clock.get_fps())))
    
        dt = clock.tick(maxFrame)/1000.0

        #process input
        events = pygame.event.get()

        main.update(dt,events)
        main.render()

        pygame.display.update()




