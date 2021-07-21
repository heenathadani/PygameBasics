import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

flag = False

font = pygame.font.SysFont("Times new Roman", 34)
text = font.render("Hello Quest - Gamers", True, (158,16,16))

while not flag :

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            flag = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            flag = True


    screen.fill((255,255,255))


    screen.blit(text,(280 - text.get_width() // 2, 240 - text.get_height() // 2))


    pygame.display.flip()
                
