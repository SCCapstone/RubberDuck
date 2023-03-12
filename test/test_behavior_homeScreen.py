import sys

sys.path.append('..')
#import pytest_bdd methods and feature file for this test
from pytest_bdd import *
import pygame

import menuStructure as menuS
from views import homeScreen
from assets import values
from assets import soundHandler

scenario('../test/features/homeScreen.feature', 'Start game')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)
    print("HERE")


@when('the player clicks the Start Game button')
def test_click_StartGame():

    print(pygame.display.get_surface().get_size()[0],
          pygame.display.get_surface().get_size()[1])
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .300, values.screenY * .765)
    print(pygame.mouse.get_pos())

    homeScreen.check_click(.253, .498, .761, .797, soundHandler.SFXHandler(),
                           menuS.menu.GAME)


@then('the game should start')
def test_game_start():
    print(pygame.mouse.get_pos())
    assert menuS.get_game_menu() == menuS.menu.GAME


#we will be able to paremeterize this one test to work for all scenarios in the feature (swtich to all other screens)
