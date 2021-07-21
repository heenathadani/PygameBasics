import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width,height))

flag = False

while not flag :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True

    pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,30,60,80))

    pygame.display.flip()
    #pygame.display.update()
