import sys

sys.path.append('..')
from pytest_bdd import *
import pygame

import menuStructure as menuS
from views import gameOverScreen
from fileio import settingIO
from assets import values

global value_passer

scenario('../test/features/gameOverScreen.feature',
         'Clicking "Home"')

@given('The Game Over Screen is displayed')
def test_gameOver_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.GAMEOVER)

@when('the user clicks the "Home" option')
def test_click_Home():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    
    remainHeight = screen.get_height() - screen.get_height() / 16 * 4
    buttonHeight = (remainHeight - 200) / 4
    buttonWidth = screen.get_width() / 2.3
    buttonX = screen.get_width() / 2 - buttonWidth / 2
    buttonY = screen.get_height() / 16 * 4
    button1 = (buttonX, buttonY)
    mouseCords = (button1[0] + 1, button1[1] + 1)
    # Move mouse to the button
        
@then('the user should be taken to the Home screen')
def test_go_to_home():
    global value_passer
    
########################################################################################

scenario('../test/features/gameOverScreen.feature',
         'Clicking "New Game"')

@given('The Game Over Screen is displayed')
def test_gameOver_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.GAMEOVER)

@when('the user clicks the "New Game" option')
def test_click_NewGame():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    
    remainHeight = screen.get_height() - screen.get_height() / 16 * 4
    buttonHeight = (remainHeight - 200) / 4
    buttonWidth = screen.get_width() / 2.3
    buttonX = screen.get_width() / 2 - buttonWidth / 2
    buttonY = screen.get_height() / 16 * 4
    button2 = (buttonX, buttonY + buttonHeight + 50)
    mouseCords = (button2[0] + 1, button2[1] + 1)
    # Move mouse to the button
        
@then('the game should restart from the beginning')
def test_restart_game():
    global value_passer
    
########################################################################################

scenario('../test/features/gameOverScreen.feature',
         'Clicking "Share Score"')

@given('The Game Over Screen is displayed')
def test_gameOver_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.GAMEOVER)

@when('the user clicks the "Share Score" option')
def test_click_ShareScore():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    
    remainHeight = screen.get_height() - screen.get_height() / 16 * 4
    buttonHeight = (remainHeight - 200) / 4
    buttonWidth = screen.get_width() / 2.3
    buttonX = screen.get_width() / 2 - buttonWidth / 2
    buttonY = screen.get_height() / 16 * 4
    button3 = (buttonX, buttonY + buttonHeight *2 + 100)
    mouseCords = (button3[0] + 1, button3[1] + 1)
    # Move mouse to the button
        
@then('the Share Score Graphic should be displayed')
def test_display_ShareScoreGraphic():
    global value_passer
    
########################################################################################

scenario('../test/features/gameOverScreen.feature',
         'Clicking "High Score Board"')

@given('The Game Over Screen is displayed')
def test_gameOver_Screen():
    settingIO.load_settings(values.SETTING_PATH)

    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()  #print screenX, screenY
    menuS.set_game_menu(menuS.menu.GAMEOVER)

@when('the user clicks the "High Score Board" option')
def test_click_HighScoreBoard():
    global value_passer
    # Calculate the position of the button
    screen = pygame.display.get_surface()
    
    remainHeight = screen.get_height() - screen.get_height() / 16 * 4
    buttonHeight = (remainHeight - 200) / 4
    buttonWidth = screen.get_width() / 2.3
    buttonX = screen.get_width() / 2 - buttonWidth / 2
    buttonY = screen.get_height() / 16 * 4
    button4 = (buttonX, buttonY + buttonHeight *3 + 150)
    mouseCords = (button4[0] + 1, button4[1] + 1)
    # Move mouse to the button
        
@then('the user should be taken to the High Score screen')
def test_go_to_HighScores():
    global value_passer