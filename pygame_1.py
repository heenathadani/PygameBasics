import pygame #includes all the pygame in-built functions and classes
pygame.init()#initialises the pygame module

white = (255,255,255) #sets the gaming window bg as white in the RGB Mode

width = 800 #width of the gaming window
height = 800 #height of the gaming window

screen = pygame.display.set_mode((width,height)) #sets the gaming window
pygame.display.set_caption("PYGAME BASICS") #names the gaming window

image = pygame.image.load(r'C:\Users\Heena Thadani\Downloads\rog.jpg') #loads image

#flag = False

while True :

    screen.fill(white) #fills the screen bg with white color
    screen.blit(image,(0,0)) #uploads the image to our screen at 0,0 coordinate
    
    for event in pygame.event.get() : #for every event that we actually press on the keyboard, we recieve this as a list 
        if event.type == pygame.QUIT: #if we press X in the top right corner of the screen
            pygame.quit() #quit the window
            #flag = True
            #quit()
        #pygame.display.flip()
        pygame.display.update()#updates the gaming window


