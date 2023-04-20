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
    screen = pygame.display.get_surface()
    left, right, subtitleFont = statScreen.screen_no_button(screen)
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    mouse_pos = shareCords[0] + 1, shareCords[1] + 1
    widthButton = (right - left - 40) / 3
    pygame.mouse.set_pos(mouse_pos)
    mouse_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=mouse_pos)
    pygame.event.post(mouse_event)
    value_passer = statScreen.check_click(shareCords, widthButton)

    
@then('the share stats graphic should be displayed')
def test_shareStats_graphic():
    global value_passer
    assert value_passer == True
    value_passer = None
    
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
    screen = pygame.display.get_surface()
    left, right, subtitleFont = statScreen.screen_no_button(screen)
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    widthButton = (right - left - 40) / 3
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    mouse_pos = homeCords[0] + 1, homeCords[1] + 1
    pygame.mouse.set_pos(mouse_pos)
    mouse_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=mouse_pos)
    pygame.event.post(mouse_event)
    value_passer = statScreen.check_click(homeCords, widthButton)
    
@then('the home screen should be displayed')
def test_return_home():
    global value_passer
    assert value_passer == True
    value_passer = None
    
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
    screen = pygame.display.get_surface()
    left, right, subtitleFont = statScreen.screen_no_button(screen)
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    widthButton = (right - left - 40) / 3
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)
    mouse_pos = quitCoords[0] + 1, quitCoords[1] + 1
    pygame.mouse.set_pos(mouse_pos)
    mouse_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=mouse_pos)
    pygame.event.post(mouse_event)
    value_passer = statScreen.check_click(quitCoords, widthButton)
    
@then('the application should close')
def test_stat_quit():
    global value_passer
    assert value_passer == True
    value_passer = None