import pygame, time
from Typewriter_Text_Class import *

pygame.init()

WHITE = (255, 255, 255, 255)

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()


fontsize = 10

FONT = pygame.font.Font("Assets\Font\Grand9k Pixel.tff", fontsize)

text = 

while True:
    clock.tick(60)


    screen.fill(WHITE)




    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            