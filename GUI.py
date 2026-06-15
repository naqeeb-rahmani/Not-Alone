import pygame 
from Text_Class import *

class GUI:
    def __init__(self, x, y, WIDTH):
        self.x = x; self.y = y

        self.HEIGHT = 40
        self.WIDTH = WIDTH

        self.font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", 25)

        self.rect = pygame.rect.Rect(x, y, WIDTH, self.HEIGHT)

        self.text_list = []

        self.finished_writing = False



    def draw(self, screen, colour_rect, colour_text):
        pygame.draw.rect(screen, (colour_rect), self.rect)
        text = self.font.render("".join(self.text_list), True, colour_text)

        screen.blit(text, (self.x + 5, self.y))

#the function below needs to be placed in the "for events" loop
    def inputs(self, event): #only numbers and full stops because the player will only be typing the ip of the host 
        if event.type == pygame.KEYDOWN:
            if len(self.text_list) < 15:
                if event.unicode.isdigit():
                    self.text_list.append(str(event.unicode))

                if event.key == pygame.K_PERIOD:
                    self.text_list.append(".")

            if event.key == pygame.K_BACKSPACE:
                if len(self.text_list) > 0:
                    self.text_list.pop(-1)

            if event.key == pygame.K_RETURN:
                self.finished_writing = True
                
    
def text_box_effect(game, x):
    if x.finished_writing == True:
        game.mode 