import pygame
import os

# Colors
COLOR_Purple = (46, 41, 78)
COLOR_Pink = (204, 167, 162)
COLOR_Yellow = (233, 215, 88)
COLOR_Orange = (175, 67, 25)
COLOR_Red = (119, 32, 20)
COLOR_White = (255, 255, 255)

# Fonts
FONT_Ethnocentric = os.path.join("assets", "fonts", "Ethnocentric.ttf")
FONT_EthnocentricItalic = os.path.join("assets", "fonts",
                                       "EthnocentricItalic.ttf")

# Screen Size defaults to 0 until setScreenSize is called
screenX = 0
screenY = 0


# Set Screen Size
def setScreenSize(x, y):
    global screenX, screenY
    screenX = x
    screenY = y
