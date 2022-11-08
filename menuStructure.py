from enum import Enum


class Menu(Enum):
    HOME = 1
    STAT = 2
    GAME = 3
    CUSTOMIZE = 4
    HIGH_SCORE = 5
    SETTING = 6
    QUIT = 7


global Game_Menu


def setGameMenu(menu):
    global Game_Menu
    Game_Menu = menu


def getGameMenu():
    global Game_Menu
    return Game_Menu
