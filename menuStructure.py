from enum import Enum
import time


# Set the menu structure
class Menu(Enum):
    HOME = 1
    STAT = 2
    GAME = 3
    CUSTOMIZE = 4
    HIGH_SCORE = 5
    SETTING = 6
    QUIT = 7


global Game_Menu


# Set the menu structure
def setGameMenu(menu):
    global Game_Menu
    Game_Menu = menu


# Get the menu structure
def getGameMenu():
    global Game_Menu
    return Game_Menu


# make method to prevent double click
def doubleClickPreventer():
    time.sleep(.1)
