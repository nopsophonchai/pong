import pygame 
import sys 

pygame.init()

กว้าง = 1024
ยาว = 768

screen = pygame.display.set_mode((1024, 768))

pygame.display.set_caption("Wan Yen")

font = pygame.font.SysFont("Comic Sans MS", 45)

img = pygame.image.load('cottong.png')

pyramid = pygame.image.load('pyramid.jpg')
pyramid = pygame.transform.scale(pyramid, (กว้าง,ยาว))
text = 'dwdw'
x = 300
y = 300

smallFont = pygame.font.SysFont("Comic Sans MS", 10)
bigFont = pygame.font.SysFont("Comic Sans MS", 60)

first = "Welcome to your life"
second = "There's no turning back"

highFirst = True

while True:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            # if key == 'w':
            #     y -= 1
            # if key == 's':
            #     y += 1
            # if key == 'a':
            #     x -= 1
            # if key == 'd':
            #     x += 1
                

            #     pygame.quit()
            #     sys.exit()
            # print(f'{pygame.key.name(event.key)}')
            text = pygame.key.name(event.key)
            if event.key == pygame.K_DOWN:
                print("yes")
                highFirst = False
            if event.key == pygame.K_UP:
                print("no")
                highFirst = True

        
        
    screen.fill((123,123,123))
    if highFirst:
        firstRender = bigFont.render(first,False,(50,50,0))
        secondRender = bigFont.render(second,False,(50,75,0))
    else:
        firstRender = smallFont.render(first,False,(50,50,0))
        secondRender = smallFont.render(second,False,(50,75,0))

    text_render = font.render(text, False, (0,255,0))
    screen.blit(pyramid,(0,0))
    screen.blit(firstRender,(50,50))
    screen.blit(secondRender,(50,75))
    screen.blit(text_render,(100,100))

    screen.blit(img, (x,y))
    pygame.display.update()

    pass





