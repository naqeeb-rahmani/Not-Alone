import pygame

BLACK = (0, 0, 0, 255)
GREYish = (50, 50, 50, 255)

pygame.init()

font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", 24)

class Typewriter_Text:
    def __init__(self, text_pos, instruction_text_for_pressing_enter_pos, speed_per_second,text, texts, if_single_text_true_or_false):
        self.text_pos = text_pos
        self.text = text
        self.texts = texts

        self.fontsize = 24        
        self.font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", self.fontsize)

        self.fullydisplayedtext = False

        self.next_text_text_pos = instruction_text_for_pressing_enter_pos

        self.next_text_text = self.font.render("Press Enter to Continue...", True, GREYish)

        self.timer = 0 #time in seconds

        #used when given a list of numbers
        self.currenttextnumber = 0
        if if_single_text_true_or_false:
            self.currenttext = text
        else:
            self.currenttext = texts[self.currenttextnumber]

        self.totallength = len(self.currenttext)
        self.currentlength = 0

        if if_single_text_true_or_false:
            self.currentdisplaytext = self.font.render(text[0:self.currentlength], True, BLACK)
        else:
            self.currentdisplaytext = self.font.render(texts[self.currenttextnumber][0:self.currentlength], True, BLACK)

        self.single_text = if_single_text_true_or_false

        self.speed_per_second = speed_per_second

    def FullyDisplayedText(self):
        return self.fullydisplayedtext

    def GetLengthOfCurrentText(self):
        return self.currentlength
    
    def GetLengthOfDisplayedText(self):
        return self.currentlength
    
    def UpdateTotalLength(self):
        self.totallength = len(self.currenttext)

    def DrawAndUpdate(self, screen, deltatime):
        self.timer += deltatime

        if self.timer >= (60/self.speed_per_second):
            self.timer = 0
            if(self.GetLengthOfDisplayedText() < self.totallength):
                self.currentlength += 1

            if self.single_text:
                self.currentdisplaytext = self.font.render(self.text[0:self.currentlength], True, BLACK)
            else:
                self.currentdisplaytext = self.font.render(self.texts[self.currenttextnumber][0:self.currentlength], True, BLACK)

        screen.blit(self.currentdisplaytext, self.text_pos)

        if self.GetLengthOfDisplayedText() >= self.totallength and self.single_text == False:
            self.fullydisplayedtext = True
            if self.currenttextnumber < (len(self.texts)-1):
                screen.blit(self.next_text_text, self.next_text_text_pos)
            

    def NextText(self, event): #used when having a list of texts
        
        if self.GetLengthOfCurrentText() == self.totallength:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.currenttextnumber < (len(self.texts)-1):
                        self.currenttextnumber+=1
                        self.currentlength = 0
                        self.totallength = len(self.texts[self.currenttextnumber])
                        self.fullydisplayedtext = False



        
