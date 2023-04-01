"""summary: The main file for the game
"""
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
from views import gameScreen

from fileio import settingIO
from fileio import highScoreIO
from fileio import statsIO
from fileio import customizationIO

pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Ducks In Space")
pygame.display.update()



statsIO.load_stats()
settingIO.load_settings(values.SETTING_PATH)
highScoreIO.load_high_scores()
values.setStartTime()
customizationIO.load_customization()
values.total_coins = customizationIO.coins
values.current_skin = customizationIO.current_skin
values.current_background = customizationIO.current_background

# Initialize the mixer
noises = soundHandler.SFXHandler()

menuS.set_game_menu(menuS.menu.HOME)
values.set_screen_size(pygame.display.get_surface().get_size()[0],
                       pygame.display.get_surface().get_size()[1])


def main():
    """summary: main loop for game
    """
    startingDuck = 0
    startingTab = 0
    # Keep the game open until the user closes it
    noises.playMusic("menus")
    noises.music_volume(settingIO.Music_Volume)
    ran = False
    visitedHighScore = False
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
            if visitedHighScore:
                noises.playMusic("menus")
                visitedHighScore = False
            homeScreen.home_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.STAT:
            statScreen.start_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.GAME:
            visitedHighScore = False
            if not ran:
                noises.playMusic("gameplay")
            ran = True
            gameScreen.gameScreen()
        elif menuS.get_game_menu() == menuS.menu.CUSTOMIZE:
            startingDuck, startingTab = customizeScreen.customize_screen(
                noises, startingDuck, startingTab)
        elif menuS.get_game_menu() == menuS.menu.HIGH_SCORE:
            if values.newHighScore and not visitedHighScore:
                noises.playMusic("highScore")
                visitedHighScore = True
            highScoreScreen.high_score_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.SETTING:
            settingScreen.settings_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.GAMEOVER:
            gameOverScreen.start_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.QUIT:
            statsIO.save_stats()
            settingIO.save_settings()
            customizationIO.save_customization()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()


def quit_game():
    """summary: quits the game
    """
    statsIO.save_stats()
    settingIO.save_settings()
    customizationIO.save_customization()
    pygame.quit()
    sys.exit()
