import sys
import time

sys.path.append('..')
from pytest_bdd import *
import pygame

import menuStructure as menuS
from assets import soundHandler
from views import gameScreen
global value_passer, game
#scenario('../test/features/gameScreen.feature', '<scenario name>')
#Use given when then structure for tests

@scenario('../test/features/gameScreen.feature', 'Start Game')

@given('the game is called to splash screen')
def test_game_is_running():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.GAME)
    
@when('the player presses the start button') 
def test_click_start():
    global value_passer
    game = gameScreen.Game() #call gameScreen function
    game.reset()
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()
    
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()

    value_passer = game
    
@then('the game should start and the game screen should appear')
def test_game_is_running():
    global value_passer
    assert value_passer.stage == value_passer.PLAYING
    value_passer = None
    
    
@scenario('../test/features/gameScreen.feature', 'Fire rocket')

@given('the game is running')
def test_game_is_running():
    global game
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.GAME)
    gameScreen.noiseMaker = soundHandler.SFXHandler()
    game = gameScreen.Game() #call gameScreen function
    game.reset()
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()
    
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()

@when('the player presses the fire button')
def test_click_rocket():
    global game
    game.duck.shoot()

@then('a rocket should be launched from the player\'s position towards where the mouse is pointing')
def test_rocket_is_fired():
    global game
    assert game.duck.rockets is not None

@scenario('../test/features/gameScreen.feature', 'Lose a heart')
@given('the game is running')
def test_game_is_running():
    global game
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.GAME)
    gameScreen.noiseMaker = soundHandler.SFXHandler()
    game = gameScreen.Game() #call gameScreen function
    game.reset()
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()
    
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()

@when('the player collides with an enemy')
def test_collide():
    global game
    game.duck.takeDamage(1)
    
@then('the player should lose a heart')
def test_heart_is_lost():
    global game
    assert game.duck.health == 2
    
@scenario('../test/features/gameScreen.feature', 'Pause Game')
@given('the game is running')
def test_game_is_running():
    global game
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.GAME)
    gameScreen.noiseMaker = soundHandler.SFXHandler()
    game = gameScreen.Game()
    game.reset()
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()

@when('the player presses the pause button')
def test_click_pause():
    global game
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()
    
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()
    
@then('the game should pause and the pause screen should appear')
def test_game_is_paused():
    global game
    assert game.stage == game.PAUSED
    game.reset()


@scenario('../test/features/gameScreen.feature', 'Lose the game')   
@given('the game is running')
def test_game_is_running():
    global game
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.GAME)
    gameScreen.noiseMaker = soundHandler.SFXHandler()
    game = gameScreen.Game()
    game.reset()
    # Simulate an escape key click
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.process_events()


@when('the player loses all hearts')
def test_lose_all_hearts():
    global game
    game.duck.takeDamage(3)
    game.process_events()
    game.update()

@then('the game should end and the game over screen should appear')
def test_game_is_over():
    global game
    assert game.stage == game.GAME_OVER

