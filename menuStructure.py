from enum import Enum
import time


# Set the menu structure
class menu(Enum):
    HOME = 1
    STAT = 2
    GAME = 3
    CUSTOMIZE = 4
    HIGH_SCORE = 5
    SETTING = 6
    QUIT = 7
    GAMEOVER = 8


global Game_Menu


# Set the menu structure
def set_game_menu(menu):
    global Game_Menu
    Game_Menu = menu


# Get the menu structure
def get_game_menu():
    global Game_Menu
    return Game_Menu


# make method to prevent double click
def double_click_preventer():
    time.sleep(.1)
