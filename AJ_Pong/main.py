import pygame, sys, random, math

from constant import *
from Ball import Ball
from Paddle import Paddle
from shroom import Shroom
import math


class GameMain:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.music_channel = pygame.mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        
        self.sounds_list = {
            'paddle_hit': pygame.mixer.Sound('../AJ_Pong/sounds/paddle_hit.wav'),
            'score': pygame.mixer.Sound('../AJ_Pong/sounds/score.wav'),
            'wall_hit': pygame.mixer.Sound('../AJ_Pong/sounds/wall_hit.wav')
        }

        self.small_font = pygame.font.Font('./font.ttf', 24)
        self.large_font = pygame.font.Font('./font.ttf', 48)
        self.score_font = pygame.font.Font('./font.ttf', 96)

        self.player1_score = 0
        self.player2_score = 0

        self.serving_player = 1
        self.winning_player = 0

        self.player1 = Paddle(self.screen, 30, 90, 15, 100)
        self.player2 = Paddle(self.screen, WIDTH - 30, HEIGHT - 90, 15, 100)

        self.ball = Ball(self.screen, WIDTH/2 - 6, HEIGHT/2 - 6, 12, 12)


        self.game_state = 'start'
        self.createShroom = False
        self.playerCollide = 0
        self.shroomCollision = False
        self.time = 0
        self.pick = False
        self.ai = False
        self.mediumai = False
        self.mediumTime = 0
        self.bounceLocation = 0
        self.bounce = False
        self.yImpact = 0
        self.initialServe = True

    def update(self, dt, events, runtime):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_state == 'start':
                        self.game_state = 'serve'
                    elif self.game_state == 'serve':
                        self.game_state = 'play'
                    elif self.game_state == 'done':
                        self.game_state = 'serve'
                        self.ball.Reset()

                        self.player1_score=0
                        self.player2_score=0
                        # print(self.player1_score)

                        if self.winning_player == 1:
                            self.serving_player = 2
                        else:
                            self.serving_player = 1


        if self.game_state == 'serve':
            self.initialServe = True
            self.createShroom = False
            self.time = 0
            self.ball.dy = random.uniform(-150, 150)
            if self.serving_player == 1:
                self.ball.dx = random.uniform(420, 600)
            else:
                self.ball.dx = -random.uniform(420, 600)

        elif self.game_state == 'play':
            self.time += 1
            # print(shroomCollision)
            # print(self.createShroom)
            if self.initialServe:
                self.initialServe = False
                bounceSpot = (self.ball.rect.x, self.ball.rect.y, self.ball.dx)
                if bounceSpot[2] > 0:
                        print('--------------')
                        print('called')
                        self.bounce = False
                        # theta = math.atan(self.ball.dy,self.ball.dx)
                        distance = abs(bounceSpot[0] - self.player2.rect.x)
                        timeImpact = distance / self.ball.dx
                        #Top
                        # if self.ball.dy > 0:
                        self.yImpact = int(bounceSpot[1] + (self.ball.dy * timeImpact))
            if self.mediumai:
                self.mediumTime += 1
                # print(f'ball pos {self.ball.rect.x}')
                if not self.pick:
                    self.player2.rect.y = HEIGHT // 2
                    self.player2.dy = random.choice([-PADDLE_SPEED,PADDLE_SPEED])
                    self.pick = True
                # print(f'Paddle Speed {self.player2.dy}')
                # if (self.mediumTime == random.randint(100,1000) or self.mediumTime % 100 == 0) and self.ball.rect.x <= WIDTH // 2:
                #     print('hi')
                #     self.mediumTime = 0
                #     self.player2.dy = -PADDLE_SPEED
                # if self.ball.rect.y < HEIGHT // 2:
                #     if self.player2.rect.y + self.player2.rect.height >= HEIGHT //1.5:
                #         self.player2.dy = -PADDLE_SPEED
                #     elif self.player2.rect.y <= 0:
                #         self.player2.dy = PADDLE_SPEED
                # if self.ball.rect.y >= HEIGHT // 2:
                #     if self.player2.rect.y + self.player2.rect.height <= HEIGHT //1.5:
                #         self.player2.dy = PADDLE_SPEED
                #     elif self.player2.rect.y >= HEIGHT:
                #         self.player2.dy = -PADDLE_SPEED
                if self.bounce:
                    bounceSpot = (self.ball.rect.x, self.ball.rect.y, self.ball.dx)
                    #Bouncing towards AI
                    if bounceSpot[2] > 0:
                        print('--------------')
                        print('called')
                        self.bounce = False
                        # theta = math.atan(self.ball.dy,self.ball.dx)
                        distance = abs(bounceSpot[0] - self.player2.rect.x)
                        timeImpact = distance / self.ball.dx
                        #Top
                        # if self.ball.dy > 0:
                        self.yImpact = int(bounceSpot[1] + (self.ball.dy * timeImpact))
                        # elif self.ball.dy < 0:
                        #     self.yImpact = int(bounceSpot[1] - self.ball.dy * timeImpact)
                        print(f'Predicted Impact: {self.yImpact}')
                        print(f'Ball Speed: {self.ball.dy}')
                        print(f'Current Position: {self.player2.rect.y}')
                        print('--------------')
                if self.yImpact > (self.player2.rect.y + self.player2.rect.height // 2):
                    print('going up')
                    self.player2.dy = PADDLE_SPEED
                if self.yImpact < (self.player2.rect.y + self.player2.rect.height // 2):
                    self.player2.dy = -PADDLE_SPEED
                
                if abs(self.yImpact - (self.player2.rect.y + self.player2.rect.height // 2)) <= 10:
                    print('The paddle is on spot')
                    self.player2.dy = 0
                            # self.bounce = False
                        #Disablet this to make it cheating basically
                        # self.bounce = False
                        

                # if self.player2.rect.y + self.player2.rect.height >= HEIGHT:
                #         self.player2.dy = -PADDLE_SPEED
                # elif self.player2.rect.y <= 0:
                #     self.player2.dy = PADDLE_SPEED

            if self.ai:
                if not self.pick:
                    self.player2.rect.y = HEIGHT // 2
                    self.player2.dy = random.choice([-PADDLE_SPEED,PADDLE_SPEED])
                    self.pick = True
                if self.player2.rect.y + self.player2.rect.height >= HEIGHT:
                    self.player2.dy = -PADDLE_SPEED
                    print('yes')
                elif self.player2.rect.y <= 0:
                    self.player2.dy = PADDLE_SPEED
                    print('no')

            if not self.createShroom:
                if self.time == 100:
                    print('Shroom Generated')
                    self.shroom = Shroom(self.screen, random.randint(100,1180), random.randint(100,620))
                    self.createShroom = True
                    
            # print(self.time)
            
            if self.ball.Collides(self.player1):
                self.playerCollide = 1
                self.ball.dx = -self.ball.dx * 1.03  # reflect speed multiplier
                self.ball.rect.x = self.player1.rect.x + 15

                if self.ball.dy < 0:
                    self.ball.dy = -random.uniform(30, 450)
                else:
                    self.ball.dy = random.uniform(30, 450)
                self.bounce = True 
                self.bounceLocation = 3
                self.music_channel.play(self.sounds_list['paddle_hit'])

            if self.ball.Collides(self.player2):
                self.playerCollide = 2
                self.ball.dx = -self.ball.dx * 1.03
                self.ball.rect.x = self.player2.rect.x - 12
                if self.ball.dy < 0:
                    self.ball.dy = -random.uniform(30, 450)
                else:
                    self.ball.dy = random.uniform(30, 450)

                self.music_channel.play(self.sounds_list['paddle_hit'])

            if self.createShroom:
                if self.ball.Collides(self.shroom):
                    self.createShroom = False
                    self.time = 0
                    if self.player1.height < 600 and self.player2.height < 600:
                        if self.playerCollide == 1:
                            self.player1.rect.height += 10
                        elif self.playerCollide == 2:
                            self.player2.rect.height += 10
                    
                    
                    

            # ball hit top wall
            if self.ball.rect.y <= 0:
                self.bounceLocation = 1
                self.bounce = True
                self.ball.rect.y = 0
                self.ball.dy = -self.ball.dy
                self.music_channel.play(self.sounds_list['wall_hit'])

            # ball hit bottom wall, 12 represents ball size
            if self.ball.rect.y >= HEIGHT - 12:
                self.bounceLocation = 2
                self.bounce = True
                self.ball.rect.y = HEIGHT - 12
                self.ball.dy = -self.ball.dy
                self.music_channel.play(self.sounds_list['wall_hit'])

            if self.ball.rect.x < 0:
                self.serving_player = 1
                self.player2_score += 1
                self.music_channel.play(self.sounds_list['score'])
                if self.player2_score==WINNING_SCORE:
                    self.winning_player=2
                    self.game_state='done'
                else:
                    self.game_state = 'serve'
                    self.ball.Reset()

            if self.ball.rect.x > WIDTH:
                self.serving_player = 2
                self.player1_score += 1
                self.music_channel.play(self.sounds_list['score'])
                if self.player1_score==WINNING_SCORE:
                    self.winning_player=1
                    self.game_state='done'
                else:
                    self.game_state = 'serve'
                    self.ball.Reset()

        key = pygame.key.get_pressed()
        if key[pygame.K_o]:
            if self.ai:
                self.ai = False
            else:
                self.ai = True
        if key[pygame.K_i]:
            if self.mediumai:
                self.mediumai = False
            else:
                self.mediumai = True

        if key[pygame.K_p]:
            # previousX = self.ball.dx
            # previousY = self.ball.dy
            self.ball.dx = 0
            self.ball.dy = 0
        # if key[pygame.K_LEFTBRACKET]:
        #     self.ball.dx = previousX
        #     self.ball.dy = previousY
        if key[pygame.K_w]:
            self.player1.dy = -PADDLE_SPEED
        elif key[pygame.K_s]:
            self.player1.dy = PADDLE_SPEED
        else:
            self.player1.dy = 0

        if not self.ai and not self.mediumai:
            if key[pygame.K_UP]:
                self.player2.dy = -PADDLE_SPEED
            elif key[pygame.K_DOWN]:
                self.player2.dy = PADDLE_SPEED
            else:
                self.player2.dy = 0
        
        


        if self.game_state == 'play':
            self.ball.update(dt)

        self.player1.update(dt)
        self.player2.update(dt)

    def render(self):
        self.screen.fill((40, 45, 52))
        if self.ai:
            t_welcome = self.small_font.render("AI ON", False, (255, 255, 255))
            text_rect = t_welcome.get_rect(center=(WIDTH / 2, 90))
            self.screen.blit(t_welcome, text_rect)
        if self.mediumai:
            t_welcome = self.small_font.render("AI ON", False, (255, 255, 255))
            text_rect = t_welcome.get_rect(center=(WIDTH / 2, 90))
            self.screen.blit(t_welcome, text_rect)
        if self.game_state == 'start':
            t_welcome = self.small_font.render("Welcome to Pong!", False, (255, 255, 255))
            text_rect = t_welcome.get_rect(center=(WIDTH / 2, 30))
            self.screen.blit(t_welcome, text_rect)

            t_press_enter_begin = self.small_font.render('Press Enter to begin!', False, (255, 255, 255))
            text_rect = t_press_enter_begin.get_rect(center=(WIDTH / 2, 60))
            self.screen.blit(t_press_enter_begin, text_rect)
        elif self.game_state == 'serve':
            t_serve = self.small_font.render("player" + str(self.serving_player) + "'s serve!", False, (255, 255, 255))
            text_rect = t_serve.get_rect(center=(WIDTH/2, 30))
            self.screen.blit(t_serve, text_rect)

            t_enter_serve = self.small_font.render("Press Enter to serve!", False, (255, 255, 255))
            text_rect = t_enter_serve.get_rect(center=(WIDTH / 2, 60))
            self.screen.blit(t_enter_serve, text_rect)
        elif self.game_state == 'play':
            pass
        elif self.game_state == 'done':
            t_win = self.large_font.render("player" + str(self.serving_player) + "'s wins!", False, (255, 255, 255))
            text_rect = t_win.get_rect(center=(WIDTH / 2, 30))
            self.screen.blit(t_win, text_rect)

            t_restart = self.small_font.render("Press Enter to restart", False, (255, 255, 255))
            text_rect = t_restart.get_rect(center=(WIDTH / 2, 70))
            self.screen.blit(t_restart, text_rect)

        self.DisplayScore()

        #right paddle
        self.player2.render()

        #left paddle
        self.player1.render()

        #ball
        self.ball.render()
        # self.shroom.render()

        if self.createShroom:
            # print("Shroom Rendered")
            self.shroom.render()


    def DisplayScore(self):
        self.t_p1_score = self.score_font.render(str(self.player1_score), False, (255, 255, 255))
        self.t_p2_score = self.score_font.render(str(self.player2_score), False, (255, 255, 255))
        self.screen.blit(self.t_p1_score, (WIDTH/2 - 150, HEIGHT/3))
        self.screen.blit(self.t_p2_score, (WIDTH / 2 + 90, HEIGHT / 3))

if __name__ == '__main__':
    main = GameMain()

    clock = pygame.time.Clock()

    while True:
        pygame.display.set_caption("Pong game running with {:d} FPS".format(int(clock.get_fps())))


        # elapsed time from the last call
        dt = clock.tick(MAX_FRAME_RATE)/1000.0
        runtime = pygame.time.get_ticks()
        events = pygame.event.get()
        main.update(dt, events,runtime)
        main.render()

        pygame.display.update()

