import pygame, time
from Typewriter_Text_Class import *

pygame.init()

WHITE = (255, 255, 255, 255)

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()


text = "Six Sayven"

texts = ["Six Sayven", "Six Sayven again", "Six Seven once more (lasttimee)"]

testtext = Typewriter_Text((100, 100), (0,0), 1000, text, [None, None], True)

testtexts = Typewriter_Text((100, 100), (100, 150), 1, "nothing", texts, False)

while True:
    starttime = pygame.time.get_ticks()
    clock.tick(60)


    screen.fill(WHITE)

    try:
        #testtext.DrawAndUpdate(screen, deltatime)
        testtexts.DrawAndUpdate(screen, deltatime)
    except:
        #testtext.DrawAndUpdate(screen, 0)
        testtexts.DrawAndUpdate(screen, 0)

    pygame.display.flip()


    for event in pygame.event.get():

        testtexts.NextText(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    deltatime = (pygame.time.get_ticks() - starttime)/1000
            