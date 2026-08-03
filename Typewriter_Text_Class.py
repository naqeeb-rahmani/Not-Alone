import pygame

BLACK = (0,0,0,255)

class Typewriter_Text:
    def __init__(self, x, y, speed_per_second,text, texts, if_single_text_true_or_false):
        self.x = x 
        self.y = y
        self.text = text
        self.texts = texts

        self.timer = 0 #time in seconds

        #used when given a list of numbers
        self.currenttextnumber = 0
        if if_single_text_true_or_false:
            self.currenttext = text
        else:
            self.currenttext = texts[self.currenttextnumber]

        self.totallength = len(self.currenttext)
        self.currentlength = 0

        self.fontsize = 24        
        self.font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", self.fontsize)
        if if_single_text_true_or_false:
            self.currentdisplaytext = self.font.render(text[0:self.currentlength], True, BLACK)
        else:
            self.currentdisplaytext = self.font.render(texts[self.currenttextnumber][0:self.currentlength])

        self.single_text = if_single_text_true_or_false

        self.speed_per_second = speed_per_second

    def GetLengthOfCurrentText(self):
        return len(self.currenttext)
        

    
    def DrawAndUpdate(self, screen, deltatime):
        self.timer += deltatime

        if self.timer >= (60/self.speed_per_second):
            self.timer = 0
            self.currentlength += 1

            if self.single_text:
                self.currentdisplaytext = self.font.render(self.text[0:self.currentlength], True, BLACK)
            else:
                self.currentdisplaytext = self.font.render(self.texts[self.currenttextnumber][0:self.currentlength])

        screen.blit(self.currentdisplaytext, (self.x, self.y))
        


        
