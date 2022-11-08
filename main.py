# Create Pygame ins
import pygame
import sys
import os
from pygame.locals import *

import menuStructure as menuS
from assets import values
from views import homeScreen


pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Duck In Space")
pygame.display.update()

menuS.setGameMenu(menuS.Menu.HOME)
values.setScreenSize(
    pygame.display.get_surface().get_size()[0],
    pygame.display.get_surface().get_size()[1])


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

        if menuS.getGameMenu() == menuS.Menu.HOME:
            homeScreen.homeScreen()
        elif menuS.getGameMenu() == menuS.Menu.STAT:
            pass
        elif menuS.getGameMenu() == menuS.Menu.GAME:
            pass
        elif menuS.getGameMenu() == menuS.Menu.CUSTOMIZE:
            pass
        elif menuS.getGameMenu() == menuS.Menu.HIGH_SCORE:
            pass
        elif menuS.getGameMenu() == menuS.Menu.SETTING:
            pass
        elif menuS.getGameMenu() == menuS.Menu.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
