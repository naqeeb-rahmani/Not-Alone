import pygame
from Typewriter_Text_Class import *

pygame.init()

class Story:
    def __init__(self, font):
        self.scene0 = pygame.image.load("Assets\Story\scene0 1280x720.png")
        self.scene1 = pygame.image.load("Assets\Story\scene1 1280x720.png")
        self.scene2 = pygame.image.load("Assets\Story\scene2 1280x720.png")

        self.scenes = [self.scene0, self.scene1, self.scene2]

        self.nextscenetext = font.render("Press enter to continue...", True, (150, 150, 150))

        self.backtomenutext = font.render("Press enter to go back to menu...", True, (150, 150, 150))

        self.nextscene = False

        self.fadesurface = pygame.Surface((1280, 720)); self.fadesurface.set_alpha(0)
        self.fadeopacity = 0
        self.halffadecomplete = False

        self.doctortext = font.render("Doctor:", True, (200, 200, 200))

        self.textforscene0 = ["Finally! After years of work, I made them",
                              "I made the first humanoids, not just one, but two of them",
                              "What a great start to the year", 
                              "I will finally be able to use the underground facility that I spent years on"]

        self.textscene0 = Typewriter_Text((50, 550), (900, 670), 1, None, self.textforscene0, False)
        
        self.textforscene1 = ["Time to take them to the facility so I can test their intelligence"]

        self.textscene1 = Typewriter_Text((50, 550), (900, 670), 1, None, self.textforscene1, False)

        self.textforscene2 = ["Now, I will just leave them here and see whether they are able to escape or not"]

        self.textscene2 = Typewriter_Text((50, 550), (900, 670), 1, None, self.textforscene2, False)

        self.currentscene = 0

        self.intro = True

        self.storyintrotextransparency = 0
        self.storyintrotext = font.render("Saturday, the 1st of January, 2067", True, (255, 255, 255))
        self.storyintrotext.set_alpha(self.storyintrotextransparency)
        self.storyintrocontinuetext = font.render("Press enter to continue...", True, (100, 100, 100))

        self.spotlightsfx = pygame.mixer.Sound("Assets\Audio\SoundEffects\spotlight.mp3")


    def IncreaseIntroTextTransparencyInStoryMode(self, font):

        if (self.storyintrotextransparency < 255):
            self.storyintrotextransparency += 1
            self.storyintrotext = font.render("Saturday, the 1st of January, 2067", True, (255, 255, 255))
            self.storyintrotext.set_alpha(self.storyintrotextransparency)

    def Fade(self, screen):
        if self.nextscene:

            screen.blit(self.fadesurface, (0, 0))
            
            if self.fadeopacity < 255 and self.halffadecomplete == False:
                self.fadeopacity += 5
                if self.fadeopacity == 255:
                    self.halffadecomplete = True
            elif self.halffadecomplete == True:

                if self.currentscene == 0 and self.textscene0.fullydisplayedtexts == True:
                    self.currentscene = 1
                elif self.currentscene == 1 and self.textscene1.fullydisplayedtexts == True:
                    self.currentscene = 2

                if self.fadeopacity > 0:
                    self.fadeopacity -= 5

                if self.fadeopacity == 0:
                    self.halffadecomplete = False
                    self.nextscene = False

            self.fadesurface.set_alpha(self.fadeopacity)

        


    def DisplayStoryIntroText(self, screen):
        screen.blit(self.storyintrotext, (((1280-459)/2), ((720-36)/2))) #459 is the width of the text and 36 is the height

        if(self.storyintrotextransparency >= 255):
            screen.blit(self.storyintrocontinuetext, (800, 650))

    def ContinueFromIntro(self, event):
        if(self.storyintrotextransparency >=255):
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN):
                
                self.intro = False
                pygame.mixer.Sound.play(self.spotlightsfx)
        