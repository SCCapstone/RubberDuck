#Imports
import os
import pygame
from assets import values
import menuStructure as menuS


# Runs the customize screen
def customize_screen(noises):
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Screen Position Variables
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3

    # font size for Titles = .05
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .05))

    # font size for subtitle = .03
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))

    #Customize title
    customize_text_image = titleFont.render("Customize", True, values.COLOR_Yellow)
    customizeCords = customize_text_image.get_rect(center=(screen.get_width() / 2,
                                                   screen.get_height() / 16 *
                                                   2))
    screen.blit(customize_text_image, customizeCords)



    #Coins available text
    coins_text_image = subtitleFont.render("Coins: ", True, values.COLOR_Yellow)
    coinsCords = (left + 200, screen.get_height() / 16 * 3)
    screen.blit(coins_text_image, coinsCords)

    #TODO add coin asset plus amount of coins available

    #load duck base skins
    baseDuck = pygame.image.load("assets/sprites/baseDuck.png")
    swagDuck = pygame.image.load("assets/sprites/swagDuck.png")

    #scale base skins for preview
    bigBaseDuck = pygame.transform.scale(baseDuck, (500,500))
    bigSwagDuck = pygame.transform.scale(swagDuck, (500,500))

    #TODO Preview of Duck in Current State
    screen.blit(bigBaseDuck, (screen.get_width() / 3, screen.get_height() / 4))

    #TODO Purchase / Equip Skin

    #TODO Left/Right arrows to browse skins to purchase / equip

    #TODO array of skins to purchase /equip at the bottom of the screen

    #TODO 4 boxes to change screen to purchase base skins, hats, trails, and backgrounds


    # Coordinates Home button
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos()[0] > homeCords[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * .122 and pygame.mouse.get_pos(
    )[1] > homeCords[1] and pygame.mouse.get_pos()[1] < values.screenY * .06:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))


    
    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                if homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + (right - left - 40) / 3 and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # return to home screen
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)



                
        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)


    