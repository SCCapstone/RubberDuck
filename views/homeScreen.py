import importlib
import pygame
import os
from pygame.locals import *

def startScreen():
        # Set the background to main.jpg
        background = pygame.image.load(
            os.path.join(
                "assets",
                "backgrounds",
                "main.jpg"))
        screen = pygame.display.get_surface()
        #scale the background to the screen size
        background = pygame.transform.scale(
            background,
            (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        
        # Update the screen
        pygame.display.flip()
        pygame.display.update()