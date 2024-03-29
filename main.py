"""summary: The main file for the game
"""
import sys
import pygame
import menuStructure as menuS
from easygui import *
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

# Initialize pygame
pygame.init()
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Ducks In Space")
pygame.display.update()

# Load the values
statsIO.load_stats()
settingIO.load_settings(values.SETTING_PATH)
highScoreIO.load_high_scores()
values.setStartTime()
customizationIO.load_customization()
values.total_coins = customizationIO.coins
values.current_skin_index = customizationIO.current_skin
values.current_hat_index = customizationIO.current_hat
values.current_background = values.getBG(customizationIO.current_background)

# Initialize the mixer
noises = soundHandler.SFXHandler()

# Set the menu structure
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
    firstRun = True
    visitedHighScore = False
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuS.set_game_menu(menuS.menu.QUIT)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    menuS.set_game_menu(menuS.menu.QUIT)
        if menuS.get_game_menu() == menuS.menu.HOME:
            if visitedHighScore:
                noises.playMusic("menus")
                visitedHighScore = False
            homeScreen.home_screen(noises)

            # Shows the Welcome Message on the first run
            if firstRun:
                firstRun = False
                if not statsIO.dontShow:
                    button1 = "Ok"
                    button2 = "Don't Show Again"
                    button_list = [button1, button2]
                    text = statsIO.help_text
                    output = buttonbox(text, "Ducks In Space", button_list)
                    if output == button2:
                        statsIO.dontShow = True
                        statsIO.save_stats()
        elif menuS.get_game_menu() == menuS.menu.STAT:
            statScreen.start_screen(noises)
        elif menuS.get_game_menu() == menuS.menu.GAME:
            visitedHighScore = False
            if not ran:
                noises.playMusic("gameplay")
            ran = True
            gameScreen.gameScreen(noises)
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

        # Quits the game and saves the values
        elif menuS.get_game_menu() == menuS.menu.QUIT:
            statsIO.save_stats()
            settingIO.save_settings()
            customizationIO.save_customization()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()


# Quits the game and saves the values
def quit_game():
    """summary: quits the game
    """
    statsIO.save_stats()
    settingIO.save_settings()
    customizationIO.save_customization()
    pygame.quit()
    sys.exit()
