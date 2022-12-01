#Imports
import os
import pygame
import math
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

    # font size for what to customize
    smallFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .015))

    #Customize title
    customize_text_image = titleFont.render("Customize", True,
                                            values.COLOR_Yellow)
    customizeCords = customize_text_image.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 16 * 2))
    screen.blit(customize_text_image, customizeCords)

    #Coins available text - import actaul amount from JSON
    coins_text_image = subtitleFont.render("Coins:   500", True,
                                           values.COLOR_Yellow)
    coinsCords = (left + screen.get_width()*.1215, screen.get_height() / 16 * 3)
    screen.blit(coins_text_image, coinsCords)
    #coins asset next to available coins
    coins = pygame.image.load("assets/sprites/Coin.png")
    screen.blit(coins, (coinsCords[0] +screen.get_width() *.1273, coinsCords[1]))

    #TODO add coin asset plus amount of coins available

    #load duck base skins
    purchaseSize = math.floor( screen.get_width()*.1504)
    silhouetteDuck = pygame.image.load("assets/sprites/silhouetteDuck.png")
    baseDuck = pygame.image.load("assets/sprites/baseDuck.png")
    swagDuck = pygame.image.load("assets/sprites/swagDuck.png")
    swagDuck = pygame.transform.scale(swagDuck, (purchaseSize, purchaseSize))

    #scale base skins for preview
    previewSize = math.floor(screen.get_width()*.28935)
    bigBaseDuck = pygame.transform.scale(baseDuck, (previewSize, previewSize))
    pygame.transform.scale(swagDuck, (previewSize, previewSize))
    pygame.transform.scale(silhouetteDuck, (previewSize, previewSize))

    #TODO Preview of Duck in Current State
    screen.blit(bigBaseDuck, (screen.get_width() / 3, screen.get_height() / 4))

    #TODO Purchase / Equip Skin

    #TODO Left/Right arrows to browse skins to purchase / equip
    xArr1 = math.floor(screen.get_width()*.3183)
    yArr = math.floor(screen.get_height()*.6267)
    wArr = math.floor(screen.get_width()*.0579)
    hArr = math.floor(screen.get_height()*.0895)
    sep = math.floor(screen.get_width()*.0289)
    box = math.floor(screen.get_width()*.1447)

    leftArr = pygame.image.load("assets/sprites/Back_Arrow.png")
    bigArr = pygame.transform.scale(leftArr, (wArr, hArr))
    screen.blit(bigArr, (xArr1, yArr))

    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xArr1 + wArr + sep, yArr, box, hArr), 0)

    if pygame.mouse.get_pos()[0] > xArr1 + wArr + sep and pygame.mouse.get_pos(
    )[0] < xArr1 + wArr + sep + box and pygame.mouse.get_pos(
    )[1] > yArr and pygame.mouse.get_pos()[1] < yArr + hArr:
        equip_text_image = smallFont.render("Equip", True, values.COLOR_Yellow)
    else:
        equip_text_image = smallFont.render("Equip", True, values.COLOR_Purple)
    screen.blit(equip_text_image, (xArr1 + wArr + sep + screen.get_width()*.0434, yArr + screen.get_height()*.0313))

    rightArr = pygame.transform.rotate(bigArr, 180)
    screen.blit(rightArr, (xArr1 + sep + sep + box + wArr, yArr))

    #TODO array of skins to purchase /equip at the bottom of the screen
    #will make these box objects for an array so we can move with arrows, know which ones have been purchased.
    numboxes = 10
    for i in range(numboxes):
        pygame.draw.rect(screen, values.COLOR_Pink,
                         ((i + 1) * screen.get_width()*.1157 - screen.get_width()*.0289, screen.get_height()*.7610, screen.get_width()*.0868, screen.get_width()*.0868), 0)
        if (i == 0):
            screen.blit(baseDuck, ((i + 1) * screen.get_width()*.1157 - screen.get_width()*.0607, screen.get_height()*.7117))
        elif (i == 1):
            screen.blit(swagDuck, ((i + 1) * screen.get_width()*.1157 - screen.get_width()*.0607, screen.get_height()*.7117))
        else:
            screen.blit(silhouetteDuck, ((i + 1) * screen.get_width()*.1157 - screen.get_width()*.0607, screen.get_height()*.7117))

    #4 boxes to change screen to purchase base skins, hats, trails, and backgrounds
    xCord = math.floor(screen.get_width()*.0289)
    yCord = math.floor(screen.get_height()*.1791)
    width = math.floor(screen.get_width()*.1591)
    height = math.floor(screen.get_height()*.0895)
    separation = math.floor(screen.get_height()*.0448)

    #Base Skins Box
    pygame.draw.rect(screen, values.COLOR_Pink, (xCord, yCord, width, height),
                     0)

    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord + width and pygame.mouse.get_pos(
    )[1] > yCord and pygame.mouse.get_pos()[1] < yCord + height:
        BS_text_image = smallFont.render("Base Skins", True,
                                         values.COLOR_Yellow)
    else:
        BS_text_image = smallFont.render("Base Skins", True,
                                         values.COLOR_Purple)
    screen.blit(BS_text_image, (xCord + screen.get_width()*.0174, yCord + screen.get_height()*.0313))

    #Hats Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord, yCord +
                      ((height + separation) * 1), width, height), 0)
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord + width and pygame.mouse.get_pos()[1] > (
            yCord +
        (height + separation) * 1) and pygame.mouse.get_pos()[1] < (
            yCord + height + (height + separation) * 1):
        Hats_text_image = smallFont.render("Hats", True, values.COLOR_Yellow)
    else:
        Hats_text_image = smallFont.render("Hats", True, values.COLOR_Purple)
    screen.blit(Hats_text_image,
                (xCord + screen.get_width()*.0521 , yCord + screen.get_height()*.0313 + (height + separation) * 1))

    #Trails Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord, yCord +
                      ((height + separation) * 2), width, height), 0)
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord + width and pygame.mouse.get_pos()[1] > (
            yCord +
        (height + separation) * 2) and pygame.mouse.get_pos()[1] < (
            yCord + height + (height + separation) * 2):
        Trails_text_image = smallFont.render("Trails", True,
                                             values.COLOR_Yellow)
    else:
        Trails_text_image = smallFont.render("Trails", True,
                                             values.COLOR_Purple)
    screen.blit(Trails_text_image,
                (xCord + screen.get_width()*.0405, yCord + screen.get_height()*.0313 + (height + separation) * 2))

    #Backgrounds Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord, yCord +
                      ((height + separation) * 3), width, height), 0)
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord + width and pygame.mouse.get_pos()[1] > (
            yCord +
        (height + separation) * 3) and pygame.mouse.get_pos()[1] < (
            yCord + height + (height + separation) * 3):
        Backgrounds_text_image = smallFont.render("Backgrounds", True,
                                                  values.COLOR_Yellow)
    else:
        Backgrounds_text_image = smallFont.render("Backgrounds", True,
                                                  values.COLOR_Purple)
    screen.blit(Backgrounds_text_image,
                (xCord + screen.get_width()*.0029, yCord + screen.get_height()*.0313 + (height + separation) * 3))

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
                )[0] < homeCords[0] + (right - left - screen.get_width()*.0231) / 3 and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + screen.get_height()*.0448:
                    # return to home screen
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord < pygame.mouse.get_pos(
                )[1] < yCord + height:
                    noises.playSound("quack")
                    #TODO make text red or highlight box, then switch screen to customize different asset
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (
                        height + separation) * 1 < pygame.mouse.get_pos(
                        )[1] < yCord + height + (height + separation) * 1:
                    noises.playSound("quack")
                    #TODO make text red or highlight box, then switch screen to customize different asset
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (
                        height + separation) * 2 < pygame.mouse.get_pos(
                        )[1] < yCord + height + (height + separation) * 2:
                    noises.playSound("quack")
                    #TODO make text red or highlight box, then switch screen to customize different asset
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (
                        height + separation) * 3 < pygame.mouse.get_pos(
                        )[1] < yCord + height + (height + separation) * 3:
                    noises.playSound("quack")
                    #TODO make text red or highlight box, then switch screen to customize different asset

                    #click on left arrow, move boxes to the left
                elif xArr1 < pygame.mouse.get_pos(
                )[0] < xArr1 + wArr and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    noises.playSound("quack")

                    #click on equip or buy
                elif xArr1 + sep + wArr < pygame.mouse.get_pos(
                )[0] < xArr1 + sep + wArr + box and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    noises.playSound("quack")
                    #click on right arrow, move boxes to the right
                elif xArr1 + sep + wArr + box + sep < pygame.mouse.get_pos(
                )[0] < xArr1 + sep + sep + wArr + box + wArr and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    noises.playSound("quack")

        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)
