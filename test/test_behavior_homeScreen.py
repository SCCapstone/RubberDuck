import sys
sys.path.append('..')
#import pytest_bdd methods and feature file for this test
import pytest
from pytest_bdd import *
import pygame
import menuStructure as menuS
from views import homeScreen
from assets import values
from assets import soundHandler


scenario('../test/features/homeScreen.feature', 'Start game')

@given('Game is loaded')
def test_home_Screen():
    menuS.set_game_menu(menuS.menu.HOME)
    
@when('the player clicks the Start Game button')
def test_click_StartGame():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    homeScreen.check_click(.253, .498, .761, .797, soundHandler.SFXHandler(), menuS.menu.GAME)
    #print screenX, screenY
    print(pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX*.300, values.screenY*.765)
    pygame.mouse.set_visible(True)
    print(pygame.mouse.get_pos())
    pygame.mouse.set_pressed((1, 0, 0))
    
@then('the game should start')
def test_game_start():
    assert menuS.get_game_menu() == menuS.menu.GAME

#we will be able to paremeterize this one test to work for all scenarios in the feature (swtich to all other screens)