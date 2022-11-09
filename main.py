# Create Pygame ins
import pygame
import sys
import os
from pygame.locals import *

import menuStructure as menuS
from assets import values
from views import homeScreen
from views import gameOverScreen
from views import statScreen
from views import gameScreen
from views import settingScreen


pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Ducks In Space")
pygame.display.update()

statScreen.StartLoad()

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
                menuS.setGameMenu(menuS.Menu.QUIT)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menuS.setGameMenu(menuS.Menu.QUIT)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #    x, y = pygame.mouse.get_pos()
             #   print(
             #       x / pygame.display.get_surface().get_size()[0],
             #       y / pygame.display.get_surface().get_size()[1])

        if menuS.getGameMenu() == menuS.Menu.HOME:
            homeScreen.homeScreen()
        elif menuS.getGameMenu() == menuS.Menu.STAT:
            statScreen.statScreen()
        elif menuS.getGameMenu() == menuS.Menu.GAME:
            pass
        elif menuS.getGameMenu() == menuS.Menu.CUSTOMIZE:
            pass
        elif menuS.getGameMenu() == menuS.Menu.HIGH_SCORE:
            pass
        elif menuS.getGameMenu() == menuS.Menu.SETTING:
            pass
        elif menuS.getGameMenu() == menuS.Menu.QUIT:
            statScreen.saveStats()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
