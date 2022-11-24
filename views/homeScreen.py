import pygame
import os
from assets import values
import menuStructure as menuS


def home_screen(noises):
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
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .004 and pygame.mouse.get_pos(
    )[0] < values.screenX * .097 and pygame.mouse.get_pos(
    )[1] > values.screenY * .044 and pygame.mouse.get_pos(
    )[1] < values.screenY * .074:
        STAT_image = font.render("STATS", True, values.COLOR_Yellow)
    else:
        STAT_image = font.render("STATS", True, values.COLOR_Pink)
    screen.blit(STAT_image, (values.screenX * .0065, values.screenY * .044))

    # Font for the buttons on main
    fontMenu = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .026))

    # if mouse is over game, change color to white
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .253 and pygame.mouse.get_pos(
    )[0] < values.screenX * .498 and pygame.mouse.get_pos(
    )[1] > values.screenY * .761 and pygame.mouse.get_pos(
    )[1] < values.screenY * .797:
        START_Text_Img = fontMenu.render("START GAME", True,
                                         values.COLOR_Yellow)
    else:
        START_Text_Img = fontMenu.render("START GAME", True, values.COLOR_Pink)
    screen.blit(START_Text_Img, (values.screenX * .2539, values.screenY * .75))

    # if mouse is over high score, change color to white
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .253 and pygame.mouse.get_pos(
    )[0] < values.screenX * .498 and pygame.mouse.get_pos(
    )[1] > values.screenY * .875 and pygame.mouse.get_pos(
    )[1] < values.screenY * .913:
        HS_Text_image = fontMenu.render("HIGH SCORES", True,
                                        values.COLOR_Yellow)
    else:
        HS_Text_image = fontMenu.render("HIGH SCORES", True, values.COLOR_Pink)
    screen.blit(HS_Text_image, (values.screenX * .2539, values.screenY * .868))

    # if mouse is over customize, change color to white
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .532 and pygame.mouse.get_pos(
    )[0] < values.screenX * .743 and pygame.mouse.get_pos(
    )[1] > values.screenY * .761 and pygame.mouse.get_pos(
    )[1] < values.screenY * .80:
        Cust_font_image = fontMenu.render("CUSTOMIZE", True,
                                          values.COLOR_Yellow)
    else:
        Cust_font_image = fontMenu.render("CUSTOMIZE", True, values.COLOR_Pink)
    screen.blit(Cust_font_image, (values.screenX * .533, values.screenY * .75))

    # if mouse is over setting, change color to white
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .532 and pygame.mouse.get_pos(
    )[0] < values.screenX * .707 and pygame.mouse.get_pos(
    )[1] > values.screenY * .868 and pygame.mouse.get_pos(
    )[1] < values.screenY * .925:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Yellow)
    else:
        Set_font_image = fontMenu.render("SETTINGS", True, values.COLOR_Pink)
    screen.blit(Set_font_image, (values.screenX * .533, values.screenY * .868))

    # if mouse is over quit, change color to yellow
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .872 and pygame.mouse.get_pos(
    )[0] < values.screenX * .9539 and pygame.mouse.get_pos(
    )[1] > values.screenY * .925 and pygame.mouse.get_pos(
    )[1] < values.screenY * .983:
        Quit_font_image = fontMenu.render("QUIT", True, values.COLOR_Yellow)
    else:
        Quit_font_image = fontMenu.render("QUIT", True, values.COLOR_White)
    screen.blit(Quit_font_image,
                (values.screenX * .872, values.screenY * .925))

    # temporary if mouse is over gameOver, change color to yellow
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .750 and pygame.mouse.get_pos(
    )[0] < values.screenX * .9539 and pygame.mouse.get_pos(
    )[1] > values.screenY * .05 and pygame.mouse.get_pos(
    )[1] < values.screenY * .10:
        GO_image = fontMenu.render("GAME OVER", True, values.COLOR_Yellow)
    else:
        GO_image = fontMenu.render("GAME OVER", True, values.COLOR_White)
    screen.blit(GO_image, (values.screenX * .750, values.screenY * .05))

    #Check if click is on a button
    click_handler(noises)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()


def click_handler(noises):

    if pygame.mouse.get_pressed()[0]:
        menuS.double_click_preventer()
        # if mouse click is on stat game button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .004 and pygame.mouse.get_pos(
        )[0] < values.screenX * .097 and pygame.mouse.get_pos(
        )[1] > values.screenY * .044 and pygame.mouse.get_pos(
        )[1] < values.screenY * .074:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.STAT)

        # if mouse click is on start game button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .253 and pygame.mouse.get_pos(
        )[0] < values.screenX * .498 and pygame.mouse.get_pos(
        )[1] > values.screenY * .761 and pygame.mouse.get_pos(
        )[1] < values.screenY * .797:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.GAME)

        # if mouse click is on high score button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .253 and pygame.mouse.get_pos(
        )[0] < values.screenX * .498 and pygame.mouse.get_pos(
        )[1] > values.screenY * .875 and pygame.mouse.get_pos(
        )[1] < values.screenY * .913:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.HIGH_SCORE)

        # if mouse click is on customize button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .532 and pygame.mouse.get_pos(
        )[0] < values.screenX * .743 and pygame.mouse.get_pos(
        )[1] > values.screenY * .761 and pygame.mouse.get_pos(
        )[1] < values.screenY * .80:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.CUSTOMIZE)

        # if mouse click is on setting button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .532 and pygame.mouse.get_pos(
        )[0] < values.screenX * .707 and pygame.mouse.get_pos(
        )[1] > values.screenY * .868 and pygame.mouse.get_pos(
        )[1] < values.screenY * .925:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.SETTING)

        # if mouse click is on quit button
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .872 and pygame.mouse.get_pos(
        )[0] < values.screenX * .9539 and pygame.mouse.get_pos(
        )[1] > values.screenY * .925 and pygame.mouse.get_pos(
        )[1] < values.screenY * .983:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.QUIT)

        # temporary for working if mouse click is on game over button)
        if pygame.mouse.get_pos(
        )[0] > values.screenX * .750 and pygame.mouse.get_pos(
        )[0] < values.screenX * .9539 and pygame.mouse.get_pos(
        )[1] > values.screenY * .05 and pygame.mouse.get_pos(
        )[1] < values.screenY * .100:
            noises.playSound("quack")
            menuS.set_game_menu(menuS.menu.GAMEOVER)
