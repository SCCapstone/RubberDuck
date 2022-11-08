import pygame
import os
from pygame.locals import *
from assets import values
import menuStructure as menuS


def homeScreen():
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
        int(values.screenX * .019))
    SR_text_image = font.render(
        "Session Runtime: 0:00",
        True,
        values.COLOR_White)
    screen.blit(SR_text_image, (values.screenX * .0065, values.screenY * .011))

    # if mouse is over stat, change color to white
    if pygame.mouse.get_pos()[0] > values.screenX * .004 and pygame.mouse.get_pos()[0] < values.screenX * .097 and pygame.mouse.get_pos()[
            1] > values.screenY * .044 and pygame.mouse.get_pos()[1] < values.screenY * .074:
        STAT_image = font.render("STATS", True, values.COLOR_Yellow)
    else:
        STAT_image = font.render("STATS", True, values.COLOR_Pink)
    screen.blit(STAT_image, (values.screenX * .0065, values.screenY * .044))

    fontMenu = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .026))

    if pygame.mouse.get_pos()[0] > values.screenX * .253 and pygame.mouse.get_pos()[0] < values.screenX * .498 and pygame.mouse.get_pos()[
            1] > values.screenY * .761 and pygame.mouse.get_pos()[1] < values.screenY * .797:
        START_Text_Img = fontMenu.render(
            "START GAME", True, values.COLOR_Yellow)
    else:
        START_Text_Img = fontMenu.render("START GAME", True, values.COLOR_Pink)
    screen.blit(START_Text_Img, (values.screenX * .2539, values.screenY * .75))

    if pygame.mouse.get_pos()[0] > values.screenX * .253 and pygame.mouse.get_pos()[0] < values.screenX * .498 and pygame.mouse.get_pos()[
            1] > values.screenY * .875 and pygame.mouse.get_pos()[1] < values.screenY * .913:
        HS_Text_image = fontMenu.render(
            "HIGH SCORES", True, values.COLOR_Yellow)
    else:
        HS_Text_image = fontMenu.render("HIGH SCORES", True, values.COLOR_Pink)
    screen.blit(HS_Text_image, (values.screenX * .2539, values.screenY * .868))

    if pygame.mouse.get_pos()[0] > values.screenX * .532 and pygame.mouse.get_pos()[0] < values.screenX * .743 and pygame.mouse.get_pos()[
            1] > values.screenY * .761 and pygame.mouse.get_pos()[1] < values.screenY * .80:
        Cust_font_image = fontMenu.render(
            "CUSTOMIZE", True, values.COLOR_Yellow)
    else:
        Cust_font_image = fontMenu.render("CUSTOMIZE", True, values.COLOR_Pink)
    screen.blit(Cust_font_image, (values.screenX * .533, values.screenY * .75))

    if pygame.mouse.get_pos()[0] > values.screenX * .532 and pygame.mouse.get_pos()[0] < values.screenX * .707 and pygame.mouse.get_pos()[
            1] > values.screenY * .868 and pygame.mouse.get_pos()[1] < values.screenY * .925:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Yellow)
    else:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Pink)
    screen.blit(Set_font_image, (values.screenX * .533, values.screenY * .868))

    if pygame.mouse.get_pos()[0] > values.screenX * .872 and pygame.mouse.get_pos()[0] < values.screenX * .9539 and pygame.mouse.get_pos()[
            1] > values.screenY * .925 and pygame.mouse.get_pos()[1] < values.screenY * .983:
        Quit_font_image = fontMenu.render("QUIT", True, values.COLOR_Yellow)
    else:
        Quit_font_image = fontMenu.render("QUIT", True, values.COLOR_White)
    screen.blit(
        Quit_font_image,
        (values.screenX * .872,
         values.screenY * .925))

    ChickHandler()

    # Update the screen
    pygame.display.flip()
    pygame.display.update()


def ChickHandler():

    if pygame.mouse.get_pressed()[0]:

        # if mouse is over stat, change color to white
        if pygame.mouse.get_pos()[0] > values.screenX * .004 and pygame.mouse.get_pos()[0] < values.screenX * .097 and pygame.mouse.get_pos()[
                1] > values.screenY * .044 and pygame.mouse.get_pos()[1] < values.screenY * .074:
            menuS.setGameMenu(menuS.Menu.STAT)

        if pygame.mouse.get_pos()[0] > values.screenX * .253 and pygame.mouse.get_pos()[0] < values.screenX * .498 and pygame.mouse.get_pos()[
                1] > values.screenY * .761 and pygame.mouse.get_pos()[1] < values.screenY * .797:
            menuS.setGameMenu(menuS.Menu.GAME)

        if pygame.mouse.get_pos()[0] > values.screenX * .253 and pygame.mouse.get_pos()[0] < values.screenX * .498 and pygame.mouse.get_pos()[
                1] > values.screenY * .875 and pygame.mouse.get_pos()[1] < values.screenY * .913:
            menuS.setGameMenu(menuS.Menu.HIGH_SCORE)

        if pygame.mouse.get_pos()[0] > values.screenX * .532 and pygame.mouse.get_pos()[0] < values.screenX * .743 and pygame.mouse.get_pos()[
                1] > values.screenY * .761 and pygame.mouse.get_pos()[1] < values.screenY * .80:
            menuS.setGameMenu(menuS.Menu.CUSTOMIZE)

        if pygame.mouse.get_pos()[0] > values.screenX * .532 and pygame.mouse.get_pos()[0] < values.screenX * .707 and pygame.mouse.get_pos()[
                1] > values.screenY * .868 and pygame.mouse.get_pos()[1] < values.screenY * .925:
            menuS.setGameMenu(menuS.Menu.SETTING)

        if pygame.mouse.get_pos()[0] > values.screenX * .872 and pygame.mouse.get_pos()[0] < values.screenX * .9539 and pygame.mouse.get_pos()[
                1] > values.screenY * .925 and pygame.mouse.get_pos()[1] < values.screenY * .983:
            menuS.setGameMenu(menuS.Menu.QUIT)
