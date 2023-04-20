import sys

sys.path.append('..')
#import pytest_bdd methods and feature file for this test
from pytest_bdd import *
import pygame

import menuStructure as menuS
from views import highScoreScreen
from fileio import settingIO
from assets import values

global value_passer

scenario('../test/features/highScoreScreen.feature',
         'High Score Screen - Play Again Button')


@given('I am on the High Score screen')
def test_highScore_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HIGH_SCORE)


@when('I press the Play Again button')
def test_click_StartGame():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    mouseCords = (playAgainCords[0] + 1, playAgainCords[1] + 1)
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    value_passer = highScoreScreen.checkCords(playAgainCords, widthButton)


@then('I should be on the Game screen')
def test_game_start():
    global value_passer
    assert value_passer == True

    # delete value from value_passer
    value_passer = None


########################################################################################

scenario('../test/features/highScoreScreen.feature',
         'High Score Screen - Home Button')


@given('I am on the High Score screen')
def test_highScore_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.HIGH_SCORE)


@when('I press the Home button')
def test_click_Home():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + playAgainCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    mouseCords = (homeCords[0] + 1, homeCords[1] + 1)
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    value_passer = highScoreScreen.checkCords(homeCords, widthButton)


@then('I should be on the Main Menu screen')
def test_go_to_home():
    global value_passer
    assert value_passer == True
    value_passer = None


########################################################################################


@scenario('../test/features/highScoreScreen.feature',
          'High Score Screen - Share Button')
@given('I am on the High Score screen')
def test_highScore_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.HIGH_SCORE)


@when('I press the Share button')
def test_click_Share():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + playAgainCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    shareCords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)
    mouseCords = (shareCords[0] + 1, shareCords[1] + 1)
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    value_passer = highScoreScreen.checkCords(shareCords, widthButton)


@then('I should see the Share Score graphic')
def test_go_to_share():
    global value_passer
    assert value_passer == True
    value_passer = None
