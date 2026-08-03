import pygame, time
from Typewriter_Text_Class import *

pygame.init()

WHITE = (255, 255, 255, 255)

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()


fontsize = 10

text = "six seven"

testtext = Typewriter_Text(450, 300, 1, text, [None, None], True)

while True:
    starttime = pygame.time.get_ticks()
    clock.tick(60)


    screen.fill(WHITE)

    try:
        testtext.DrawAndUpdate(screen, deltatime)
    except:
        testtext.DrawAndUpdate(screen, 0)



    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    deltatime = pygame.time.get_ticks() - starttime
            