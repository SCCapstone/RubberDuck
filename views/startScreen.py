import pygame
import viewInterface

image = pygame.image.load("../assets/backgrounds/main.jpg")


class startScreen():

    def __init__(self, image):

        self.image = image

    def getImage():

        return image

    def setImage(xImage):

        image = xImage

    def showScreen():

        pygame.display.update()
