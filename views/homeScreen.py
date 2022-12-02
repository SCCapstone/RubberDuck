"""summary: runner for home screen
"""
import pygame
import os
from assets import values
import menuStructure as menuS


def home_screen(noises):
    """summary: loop for homescreen render and controls

    Args:
        noises (SFXHandler): noise for quacks
    """
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "main.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Put Session runtime top left
    # get font from values.py 20)
    font = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .019))
    SR_text_image = font.render(
        "Session Runtime: " + str(values.sessionRunTime()), True,
        values.COLOR_White)
    screen.blit(SR_text_image, (values.screenX * .0065, values.screenY * .011))

    # if mouse is over stat, change color to white
    check_highlight([.004, .097, .044, .074, .0065, .044], values.COLOR_Yellow,
                    values.COLOR_Pink, font, screen, "STATS")

    # Font for the buttons on main
    fontMenu = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .026))

    check_highlight([.253, .498, .761, .797, .2539, .75], values.COLOR_Yellow,
                    values.COLOR_Pink, fontMenu, screen, "START GAME")
    check_highlight([.253, .498, .875, .913, .2539, .868], values.COLOR_Yellow,
                    values.COLOR_Pink, fontMenu, screen, "HIGH SCORES")
    check_highlight([.532, .743, .761, .80, .533, .75], values.COLOR_Yellow,
                    values.COLOR_Pink, fontMenu, screen, "CUSTOMIZE")
    check_highlight([.532, .707, .868, .925, .533, .868], values.COLOR_Yellow,
                    values.COLOR_Pink, fontMenu, screen, "SETTINGS")
    check_highlight([.872, .9539, .925, .983, .872, .925], values.COLOR_Yellow,
                    values.COLOR_White, fontMenu, screen, "QUIT")

    #Check if click is on a button
    click_handler(noises)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()


def check_highlight(factors, color1, color2, font, screen, text):
    """summary: checks if text is highlighted

    Args:
        factors (list): list of factors [xFac1, xFac2, yFac1, yFac2, screenFac1, screenFac2]
        color1 (tuple): color if highlighted
        color2 (tuple): color if not highlighted
        font (pygame.font): font of text
        screen (pygame.display): screen to render on
        text (str): text to render
    """
    if pygame.mouse.get_pos(
    )[0] > values.screenX * factors[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * factors[1] and pygame.mouse.get_pos(
    )[1] > values.screenY * factors[2] and pygame.mouse.get_pos(
    )[1] < values.screenY * factors[3]:
        STAT_image = font.render(text, True, color1)
    else:
        STAT_image = font.render(text, True, color2)
    screen.blit(STAT_image,
                (values.screenX * factors[4], values.screenY * factors[5]))


def click_handler(noises):
    """summary: Handles the click events on the main menu

    Args:
        noises (SFXHandler): SFXHandler object for quacks
    """
    if pygame.mouse.get_pressed()[0]:
        menuS.double_click_preventer()
        # if mouse click is on stat game button
        check_click(.004, .097, .044, .074, noises, menuS.menu.STAT)
        check_click(.253, .498, .761, .797, noises, menuS.menu.GAME)
        check_click(.253, .498, .875, .913, noises, menuS.menu.HIGH_SCORE)
        check_click(.532, .743, .761, .80, noises, menuS.menu.CUSTOMIZE)
        check_click(.532, .707, .868, .925, noises, menuS.menu.SETTING)
        check_click(.872, .9539, .925, .983, noises, menuS.menu.QUIT)
        check_click(.750, .9539, .05, .100, noises, menuS.menu.GAMEOVER)


def check_click(x1Fac, x2Fac, y1Fac, y2Fac, noises, screenChange):
    """summary: Prints out all 10 high scores to screen

    Args:
        x1Fac (float): x1 factor
        x2Fac (float): x2 factor
        y1Fac (float): y1 factor
        y2Fac (float): y2 factor
        noises (SFXHandler): SFXHandler object for quacks
        screenChange (menu): menu object for screen change
    """

    if pygame.mouse.get_pos(
    )[0] > values.screenX * x1Fac and pygame.mouse.get_pos(
    )[0] < values.screenX * x2Fac and pygame.mouse.get_pos(
    )[1] > values.screenY * y1Fac and pygame.mouse.get_pos(
    )[1] < values.screenY * y2Fac:
        noises.playSound("quack")
        menuS.set_game_menu(screenChange)
