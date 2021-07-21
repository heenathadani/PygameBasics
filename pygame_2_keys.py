import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("Keyboard Events")

flag = False
is_blue = True

x = 30
y = 40


while not flag :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            is_blue = not is_blue

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] :
        y -= 3

    if keys[pygame.K_DOWN] :
        y += 5

    if keys[pygame.K_LEFT] :
        x -= 5

    if keys[pygame.K_RIGHT] :
        x += 3

    if is_blue :
        color = (0,128,255)

    else :
        color = (255,100,0)

    pygame.draw.rect(screen,color,pygame.Rect(x,y,60,80))

    pygame.display.flip()

            

        
    
