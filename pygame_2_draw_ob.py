import pygame
from math import pi

pygame.init()

size = [500,500]

window = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Draw Function")

flag = False
clock = pygame.time.Clock()

while not flag :
    clock.tick(10) #milliseconds

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            flag = True

    window.fill((0,0,0))

    #drawing a line on the screen
    pygame.draw.line(window,(0,255,0),[0,0],[50,30],5)
    
    #drawing a rectangle outline
    pygame.draw.rect(window,(9,17,23),[75,10,50,20],2)

    #drawing a rectangle solid
    pygame.draw.rect(window,(10,100,230),[50,100,50,20])

    #drawing a ellipse outline
    pygame.draw.ellipse(window,(255,0,0),[85,230,50,20],2)

    #drawing a ellipse solid
    pygame.draw.ellipse(window,(45,60,200),[40,105,50,20])

    #drawing a triangle using the polygon function
    pygame.draw.polygon(window,(60,70,80),[[100,100],[0,200],[200,200]],5)

    #drawing a circle
    pygame.draw.circle(window,(90,200,240),[60,250],40)

    #drawing an arc
    pygame.draw.arc(window,(50,60,90),[210,75,150,125],0,pi/2,2)

    pygame.display.flip()

pygame.quit()









    
        
