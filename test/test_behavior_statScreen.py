import sys

sys.path.append('..')
#import pytest_bdd methods and feature file for this test

from pytest_bdd import *
import pygame

import menuStructure as menuS
from views import statScreen
from fileio import settingIO
from assets import values

global value_passer

scenario('../test/features/statScreen.feature',
         'Stat Screen Share Button')

@given('I am on the stats screen')
def test_stat_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.STAT)
    
@when('I press the share button')
def test_click_Share():
    global value_passer
    # Calculate the position of the button
    left, right, subtitleFont = screen_no_button(screen)
    widthButton = (right - left - 40) / 3
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)
    #mouseCords = 
    
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    
@then('the share stats graphic should be displayed')
def test_shareStats_graphic():
    global value_passer
    
########################################################################################

scenario('../test/features/statScreen.feature',
         'Stat Screen Home Button')

@given('I am on the stats screen')
def test_stat_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.STAT)
    
@when('I press the home button')
def test_click_Home():
    global value_passer
    # Calculate the position of the button
    left, right, subtitleFont = screen_no_button(screen)
    widthButton = (right - left - 40) / 3
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)
    #mouseCords = 
    
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    
@then('the home screen should be displayed')
def test_return_home():
    global value_passer
    
########################################################################################

scenario('../test/features/statScreen.feature',
         'Stat Screen Quit Button')

@given('I am on the stats screen')
def test_stat_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.STAT)
    
@when('I press the quit button')
def test_click_quit():
    global value_passer
    # Calculate the position of the button
    left, right, subtitleFont = screen_no_button(screen)
    widthButton = (right - left - 40) / 3
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)
    #mouseCords = 
    
    # Move mouse to the button
    pygame.mouse.set_pos(mouseCords)
    
@then('the application should close')
def test_stat_quit():
    global value_passer