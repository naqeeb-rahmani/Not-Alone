import pygame

pygame.init()

class Story:
    def __init__(self, font):
        self.scene1 = pygame.image.load("Assets\Story\scene1 1280x720.png")

        self.scenes = [self.scene1]

        self.storyintrotextransparency = 0
        self.storyintrotext = font.render("Wednesday, the 6th of july, 2067", True, (255, 255, 255))
        self.storyintrotext.set_alpha(self.storyintrotextransparency)

    def IncreaseIntroTextTransparencyInStoryMode(self, font):

        if (self.storyintrotextransparency < 255):
            self.storyintrotextransparency += 1
            self.storyintrotext = font.render("Wednesday, the 6th of july, 2067", True, (255, 255, 255))
            self.storyintrotext.set_alpha(self.storyintrotextransparency)



    def DisplayStoryIntroText(self, screen):
        screen.blit(self.storyintrotext, (((1280-423)/2), ((720-36)/2)))