import pygame
from Typewriter_Text_Class import *

pygame.init()

class Story:
    def __init__(self, font):
        self.scene0 = pygame.image.load("Assets\Story\scene1 1280x720.png")

        self.scenes = [self.scene0]

        self.textforscene0 = ["Finally! After years of work, I made them. I made these humanoids", "It surely took me years, even almost my whole life. But at least I did it", "Now I just need to test them somehow", "I'm thinking of putting them in some sort of facility.", "That way I will be able to test their intelligence based on whether if they escape or not"]

        self.textscene0 = Typewriter_Text((50, 600), (700, 650), 1, None, self.textforscene0, False)

        self.currentscene = 0

        self.intro = True

        self.storyintrotextransparency = 0
        self.storyintrotext = font.render("Wednesday, the 6th of july, 2067", True, (255, 255, 255))
        self.storyintrotext.set_alpha(self.storyintrotextransparency)
        self.storyintrocontinuetext = font.render("Press enter to continue...", True, (100, 100, 100))

        self.spotlightsfx = pygame.mixer.Sound("Assets\Audio\SoundEffects\spotlight.mp3")


    def IncreaseIntroTextTransparencyInStoryMode(self, font):

        if (self.storyintrotextransparency < 255):
            self.storyintrotextransparency += 1
            self.storyintrotext = font.render("Wednesday, the 6th of july, 2067", True, (255, 255, 255))
            self.storyintrotext.set_alpha(self.storyintrotextransparency)



    def DisplayStoryIntroText(self, screen):
        screen.blit(self.storyintrotext, (((1280-423)/2), ((720-36)/2)))

        if(self.storyintrotextransparency >= 255):
            screen.blit(self.storyintrocontinuetext, (800, 650))

    def ContinueFromIntro(self, event):
        if(self.storyintrotextransparency >=255):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.intro = False
                    pygame.mixer.Sound.play(self.spotlightsfx)
        