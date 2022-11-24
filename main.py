"""Class that runs menu and start up"""
# Create Pygame ins
import sys
import pygame
import menuStructure as menuS
from assets import values
from assets import soundHandler
from views import homeScreen
from views import statScreen
from views import settingScreen
from views import highScoreScreen
from views import customizeScreen
from views import gameOverScreen

from fileio import settingIO
from fileio import highScoreIO

pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Ducks In Space")
pygame.display.update()

# Initialize the mixer
noises = soundHandler.SFXHandler()

statScreen.start_load()
settingIO.load_settings(values.SETTING_PATH)
highScoreIO.load_high_scores()
values.setStartTime()

menuS.set_game_menu(menuS.menu.HOME)
values.set_screen_size(pygame.display.get_surface().get_size()[0],
                       pygame.display.get_surface().get_size()[1])
"""Runs the loop for various menu control functions"""


def main():
    # Keep the game open until the user closes it
    noises.playMusic("menus")
    noises.music_volume(settingIO.Music_Volume)
    ran = False
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuS.set_game_menu(menuS.menu.QUIT)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    menuS.set_game_menu(menuS.menu.QUIT)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #    x, y = pygame.mouse.get_pos()
            #   print(
            #       x / pygame.display.get_surface().get_size()[0],
            #       y / pygame.display.get_surface().get_size()[1])

        if menuS.get_game_menu() == menuS.menu.HOME:
            homeScreen.home_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.STAT:
            statScreen.start_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.GAME:
            if not ran:
                noises.playMusic("gameplay")
            ran = True
        elif menuS.get_game_menu() == menuS.menu.CUSTOMIZE:
            customizeScreen.customize_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.HIGH_SCORE:
            highScoreScreen.high_score_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.SETTING:
            settingScreen.settings_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.GAMEOVER:
            gameOverScreen.start_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.QUIT:
            statScreen.save_stats()
            settingIO.save_settings()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
