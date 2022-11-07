# Create Pygame ins
import pygame
import sys
import os
from pygame.locals import *

from assets import values
from views import homeScreen


pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Duck In Space")
pygame.display.update()


def main():
    # Keep the game open until the user closes it
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        homeScreen.startScreen()
        
        #print where user clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            


if __name__ == "__main__":
    main()
