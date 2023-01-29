#import pytest_bdd methods and feature file for this test
import pytest
from pytest_bdd import *

import menuStructure as menuS
from views import homeScreen
from assets import values


scenarios('../features/homeScreen.feature')

@given('Game is loaded')
def home_Screen():
    menuS.set_game_menu(menuS.menu.HOME)
    
@when('the player clicks the Start Game button')
def click_StartGame():
    homeScreen.check_click(.253, .498, .761, .797, noises, menuS.menu.GAME)
    
@then('a new game is started')
def final_view():
    assert menuS.get_game_menu == 3

#we will be able to paremeterize this one test to work for all scenarios in the feature (swtich to all other screens)