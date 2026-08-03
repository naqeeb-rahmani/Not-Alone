import pygame

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
        

        self.single_text = if_single_text_true_or_false

        self.speed_per_second = speed_per_second
    
    

        

    
    def DrawAndUpdate(self, deltatime):
        self.timer += 0

        
