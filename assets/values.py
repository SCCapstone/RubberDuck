import os
import time

global startTime
global game_score
# Colors
COLOR_Purple = (46, 41, 78)
COLOR_Pink = (204, 167, 162)
COLOR_Yellow = (233, 215, 88)
COLOR_Orange = (175, 67, 25)
COLOR_Red = (119, 32, 20)
COLOR_White = (255, 255, 255)
COLOR_Black = (0, 0, 0)

# Fonts
FONT_Ethnocentric = os.path.join("assets", "fonts", "Ethnocentric.ttf")
FONT_EthnocentricItalic = os.path.join("assets", "fonts",
                                       "EthnocentricItalic.ttf")

# Screen Size defaults to 0 until setScreenSize is called
# Screen Size defaults to 0 until setScreenSize is called
screenX = 0
screenY = 0
SCREEN_SIZE = (screenX, screenY)

SETTING_PATH = "fileio\\UserSetting.json"


# Set Screen Size
def set_screen_size(x, y):
    global screenX, screenY, SCREEN_SIZE
    screenX = x
    screenY = y
    SCREEN_SIZE = (screenX, screenY)


def sessionRunTime():
    """Returns the time the session has been running in seconds in HH:MM"""
    global startTime
    return time.strftime("%H:%M", time.gmtime(time.time() - startTime))


def setStartTime():
    """Sets the start time of the session in HH:MM"""
    global startTime
    startTime = time.time()


masterVolume = .75

def setGameScore(score):
    global game_score
    game_score = score

def resetGameScore():
    global game_score
    game_score = 0