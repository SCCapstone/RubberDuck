import importlib
import pygame
import os
from pygame.locals import *
from assets import values


def startScreen():
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join(
            "assets",
            "backgrounds",
            "main.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background,
        (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Put Session runtime top left
    # get font from values.py 20)
    font = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        30)
    SR_text_image = font.render(
        "Session Runtime: 0:00",
        True,
        values.COLOR_White)
    screen.blit(SR_text_image, (10, 10))

    # if mouse is over stat, change color to white
    if pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[
            0] < 160 and pygame.mouse.get_pos()[1] > 60 and pygame.mouse.get_pos()[1] < 90:
        STAT_image = font.render("STATS", True, values.COLOR_Yellow)
    else:
        STAT_image = font.render("STATS", True, values.COLOR_Pink)
    screen.blit(STAT_image, (10, 60))

    fontMenu = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        40)

    if pygame.mouse.get_pos()[0] > 390 and pygame.mouse.get_pos()[
            0] < 765 and pygame.mouse.get_pos()[1] > 650 and pygame.mouse.get_pos()[1] < 700:
        START_Text_Img = fontMenu.render(
            "START GAME", True, values.COLOR_Yellow)
    else:
        START_Text_Img = fontMenu.render("START GAME", True, values.COLOR_Pink)
    screen.blit(START_Text_Img, (390, 650))

    if pygame.mouse.get_pos()[0] > 390 and pygame.mouse.get_pos()[
            0] < 775 and pygame.mouse.get_pos()[1] > 750 and pygame.mouse.get_pos()[1] < 800:
        HS_Text_image = fontMenu.render(
            "HIGH SCORES", True, values.COLOR_Yellow)
    else:
        HS_Text_image = fontMenu.render("HIGH SCORES", True, values.COLOR_Pink)
    screen.blit(HS_Text_image, (390, 750))

    if pygame.mouse.get_pos()[0] > 820 and pygame.mouse.get_pos()[
            0] < 1145 and pygame.mouse.get_pos()[1] > 650 and pygame.mouse.get_pos()[1] < 700:
        Cust_font_image = fontMenu.render(
            "CUSTOMIZE", True, values.COLOR_Yellow)
    else:
        Cust_font_image = fontMenu.render("CUSTOMIZE", True, values.COLOR_Pink)
    screen.blit(Cust_font_image, (820, 650))

    if pygame.mouse.get_pos()[0] > 820 and pygame.mouse.get_pos()[
            0] < 1090 and pygame.mouse.get_pos()[1] > 750 and pygame.mouse.get_pos()[1] < 800:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Yellow)
    else:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Pink)
    screen.blit(Set_font_image, (820, 750))

    # Update the screen
    pygame.display.flip()
    pygame.display.update()
