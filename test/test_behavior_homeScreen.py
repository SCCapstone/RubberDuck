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


@when('the player clicks the Start Game button')
def test_click_StartGame():
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .300, values.screenY * .765)
    homeScreen.check_click(.253, .498, .761, .797, soundHandler.SFXHandler(),
                           menuS.menu.GAME)


@then('the game should start')
def test_game_start():
    assert menuS.get_game_menu() == menuS.menu.GAME


########################################################################################

scenario('../test/features/homeScreen.feature', 'Access Settings screen')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)


@when('the player clicks the Settings button')
def test_click_Setting():
    # move mouse to setting button
    pygame.mouse.set_pos(values.screenX * .55, values.screenY * .875)
    homeScreen.check_click(.532, .707, .868, .925, soundHandler.SFXHandler(),
                           menuS.menu.SETTING)


@then('the view switches to the settings screen')
def test_setting_start():
    assert menuS.get_game_menu() == menuS.menu.SETTING


########################################################################################

scenario('../test/features/homeScreen.feature', 'Access High Scores screen')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)


@when('the player clicks the High Scores button')
def test_click_highscore():
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .300, values.screenY * .895)
    homeScreen.check_click(.253, .498, .878, .925, soundHandler.SFXHandler(),
                           menuS.menu.HIGH_SCORE)


@then('the view switches to the high score screen')
def test_high_score():
    assert menuS.get_game_menu() == menuS.menu.HIGH_SCORE


########################################################################################

scenario('../test/features/homeScreen.feature', 'Access Customize screen')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)


@when('the player clicks the Customize button')
def test_click_customize():
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .55, values.screenY * .765)
    homeScreen.check_click(.532, .743, .761, .80, soundHandler.SFXHandler(),
                           menuS.menu.CUSTOMIZE)


@then('the view switches to the customize screen')
def test_customize():
    assert menuS.get_game_menu() == menuS.menu.CUSTOMIZE


########################################################################################

scenario('../test/features/homeScreen.feature', 'Access Stats screen')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)


@when('the player clicks the Stats button')
def test_click_stat():
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .007, values.screenY * .05)
    homeScreen.check_click(.004, .097, .044, .074, soundHandler.SFXHandler(),
                           menuS.menu.STAT)


@then('the view switches to the stats screen')
def test_stat():
    assert menuS.get_game_menu() == menuS.menu.STAT


########################################################################################

scenario('../test/features/homeScreen.feature', 'Quit game')


@given('Game is loaded')
def test_home_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.HOME)


@when('the player clicks the Quit button')
def test_click_quit():
    # move mouse to start game button
    pygame.mouse.set_pos(values.screenX * .875, values.screenY * .95)
    homeScreen.check_click(.872, .9539, .925, .983, soundHandler.SFXHandler(),
                           menuS.menu.QUIT)


@then('the application is closed')
def test_quit():
    assert menuS.get_game_menu() == menuS.menu.QUIT
