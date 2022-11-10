from enum import Enum

# Menu of different screens


class Menu(Enum):
    HOME = 1
    STAT = 2
    GAME = 3
    CUSTOMIZE = 4
    HIGH_SCORE = 5
    SETTING = 6
    QUIT = 7


global Game_Menu
"""
Sets Menu to passed in value
"""


def setGameMenu(menu):
    global Game_Menu
    Game_Menu = menu


"""
Gets current menu
"""


def getGameMenu():
    global Game_Menu
    return Game_Menu
