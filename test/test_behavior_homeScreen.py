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
    homeScreen.check_click(.253, .498, .761, .797, soundHandler.SFXHandler(), menuS.menu.GAME)
    
@then('the game should start')
def test_game_start():
    assert menuS.get_game_menu() == menuS.menu.GAME

#we will be able to paremeterize this one test to work for all scenarios in the feature (swtich to all other screens)