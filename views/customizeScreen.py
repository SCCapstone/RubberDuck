#Imports
import os
import pygame
import math
from assets import values
import menuStructure as menuS
import main as main
from fileio import customizationIO

customizationIO.load_customization()

ownedSkins = customizationIO.skins
ownedBackgrounds = customizationIO.backgrounds

normalSkins = [
    "assets/sprites/ducks/baseDuck.png", "assets/sprites/ducks/blueDuck.png",
    "assets/sprites/ducks/brownDuck.png", "assets/sprites/ducks/grayDuck.png",
    "assets/sprites/ducks/greenDuck.png", "assets/sprites/ducks/richDuck.png"
]

baseSkins = [
    "assets/sprites/ducks/baseChain.png",
    "assets/sprites/ducks/baseConstruction.png",
    "assets/sprites/ducks/baseCowboy.png",
    "assets/sprites/ducks/baseLuffy.png", "assets/sprites/ducks/baseSanta.png",
    "assets/sprites/ducks/baseSunnies.png"
]

blueSkins = [
    "assets/sprites/ducks/blueChain.png",
    "assets/sprites/ducks/blueConstruction.png",
    "assets/sprites/ducks/blueCowboy.png",
    "assets/sprites/ducks/blueLuffy.png", "assets/sprites/ducks/blueSanta.png",
    "assets/sprites/ducks/blueSunnies.png"
]

brownSkins = [
    "assets/sprites/ducks/brownChain.png",
    "assets/sprites/ducks/brownConstruction.png",
    "assets/sprites/ducks/brownCowboy.png",
    "assets/sprites/ducks/brownLuffy.png",
    "assets/sprites/ducks/brownSanta.png",
    "assets/sprites/ducks/brownSunnies.png"
]

graySkins = [
    "assets/sprites/ducks/grayChain.png",
    "assets/sprites/ducks/grayConstruction.png",
    "assets/sprites/ducks/grayCowboy.png",
    "assets/sprites/ducks/grayLuffy.png", "assets/sprites/ducks/graySanta.png",
    "assets/sprites/ducks/graySunnies.png"
]

greenSkins = [
    "assets/sprites/ducks/greenChain.png",
    "assets/sprites/ducks/greenConstruction.png",
    "assets/sprites/ducks/greenCowboy.png",
    "assets/sprites/ducks/greenLuffy.png",
    "assets/sprites/ducks/greenSanta.png",
    "assets/sprites/ducks/greenSunnies.png"
]

richSkins = [
    "assets/sprites/ducks/richChain.png",
    "assets/sprites/ducks/richConstruction.png",
    "assets/sprites/ducks/richCowboy.png",
    "assets/sprites/ducks/richLuffy.png", "assets/sprites/ducks/richSanta.png",
    "assets/sprites/ducks/richSunnies.png"
]

bgs = [
    "assets/backgrounds/base_bg.jpg", "assets/backgrounds/pixelNebula.png",
    "assets/backgrounds/pixelSpace.png"
]

# Get current skin that is equipped
current_skin_index = customizationIO.current_skin
current_hat_index = customizationIO.current_hat
current_background_index = customizationIO.current_background
tempArray = []

if current_skin_index == 0:
    tempArray = normalSkins
elif current_skin_index == 1:
    tempArray = baseSkins
elif current_skin_index == 2:
    tempArray = blueSkins
elif current_skin_index == 3:
    tempArray = brownSkins
elif current_skin_index == 4:
    tempArray = graySkins
elif current_skin_index == 5:
    tempArray = greenSkins
elif current_skin_index == 6:
    tempArray = richSkins

values.setSkin(tempArray[current_hat_index])


def loadAssets(purchaseSize):
    allSkins = []
    baseAccessories = []
    blueAccessories = []
    brownAccessories = []
    grayAccessories = []
    greenAccessories = []
    richAccessories = []
    backgrounds = []
    for x in normalSkins:
        allSkins.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in baseSkins:
        baseAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in blueSkins:
        blueAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in brownSkins:
        brownAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in graySkins:
        grayAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in greenSkins:
        greenAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in richSkins:
        richAccessories.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (purchaseSize, purchaseSize)))
    for x in bgs:
        backgrounds.append(
            pygame.transform.scale(pygame.image.load(x),
                                   (int(purchaseSize / 2), int(purchaseSize / 2))))
    return allSkins, baseAccessories, blueAccessories, brownAccessories, grayAccessories, greenAccessories, richAccessories, backgrounds


# Runs the customize screen
def customize_screen(noises, duckIndex, arrayIndex):
    ownedSkins = customizationIO.skins
    ownedBackgrounds = customizationIO.backgrounds
    startingDuck = duckIndex
    startingArray = arrayIndex

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
    coins_imported = customizationIO.coins
    coin_text = "Coins:   " + str(coins_imported)
    coins_text_image = subtitleFont.render(coin_text, True,
                                           values.COLOR_Yellow)
    coinsCords = (left + screen.get_width() * .1215,
                  screen.get_height() / 16 * 3)
    screen.blit(coins_text_image, coinsCords)
    #coins asset next to available coins
    coins = pygame.image.load("assets/sprites/Coin.png")
    coins = pygame.transform.scale(
        coins,
        (int(screen.get_width() * .035), int(screen.get_width() * .035)))
    screen.blit(coins,
                (coinsCords[0] - screen.get_width() * .05, coinsCords[1]))

    #TODO add coin asset plus amount of coins available

    #load duck base skins
    purchaseSize = int(values.screenX * .1504)
    allSkins, baseAccessories, blueAccessories, brownAccessories, grayAccessories, greenAccessories, richAccessories, backgrounds = loadAssets(
        purchaseSize)

    if arrayIndex == 0:
        currentArray = allSkins
    elif arrayIndex == 1:
        currentArray = baseAccessories
    elif arrayIndex == 2:
        currentArray = blueAccessories
    elif arrayIndex == 3:
        currentArray = brownAccessories
    elif arrayIndex == 4:
        currentArray = grayAccessories
    elif arrayIndex == 5:
        currentArray = greenAccessories
    elif arrayIndex == 6:
        currentArray = richAccessories
    elif arrayIndex == 7:
        currentArray = backgrounds
    else:
        currentArray = allSkins

    #scale base skins for preview
    previewSize = int(values.screenX * .28935)
    if arrayIndex == 7:
        previewSize = previewSize * 2 / 3

    #TODO Purchase / Equip Skin

    #TODO Left/Right arrows to browse skins to purchase / equip
    xArr1 = math.floor(screen.get_width() * .3183)
    yArr = math.floor(screen.get_height() * .6267)
    wArr = math.floor(screen.get_width() * .0579)
    hArr = math.floor(screen.get_height() * .0895)
    sep = math.floor(screen.get_width() * .0289)
    box = math.floor(screen.get_width() * .1447)

    # Add checks to see if arrow is pressed and swap to next skin
    leftArr = pygame.image.load("assets/sprites/Back_Arrow.png")
    bigArr = pygame.transform.scale(leftArr, (wArr, hArr))
    screen.blit(bigArr, (xArr1, yArr))

    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xArr1 + wArr + sep, yArr, box, hArr), 0)

    # Equip section
    # Check and see if the skin is owned
    if arrayIndex == 0:
        usedArray = normalSkins
    elif arrayIndex == 1:
        usedArray = baseSkins
    elif arrayIndex == 2:
        usedArray = blueSkins
    elif arrayIndex == 3:
        usedArray = brownSkins
    elif arrayIndex == 4:
        usedArray = graySkins
    elif arrayIndex == 5:
        usedArray = greenSkins
    elif arrayIndex == 6:
        usedArray = richSkins
    elif arrayIndex == 7:
        usedArray = bgs
    else:
        usedArray = normalSkins

    if usedArray[startingDuck] in ownedSkins or usedArray[
            startingDuck] in ownedBackgrounds:
        # Skin is owned, show equip
        if pygame.mouse.get_pos(
        )[0] > xArr1 + wArr + sep and pygame.mouse.get_pos(
        )[0] < xArr1 + wArr + sep + box and pygame.mouse.get_pos(
        )[1] > yArr and pygame.mouse.get_pos()[1] < yArr + hArr:
            equip_text_image = smallFont.render("Equip", True,
                                                values.COLOR_Yellow)
        else:
            equip_text_image = smallFont.render("Equip", True,
                                                values.COLOR_Purple)
        screen.blit(equip_text_image,
                    (xArr1 + wArr + sep + screen.get_width() * .0434,
                     yArr + screen.get_height() * .0313))
    else:
        # Skin is unowned, show purchase option
        if pygame.mouse.get_pos(
        )[0] > xArr1 + wArr + sep and pygame.mouse.get_pos(
        )[0] < xArr1 + wArr + sep + box and pygame.mouse.get_pos(
        )[1] > yArr and pygame.mouse.get_pos()[1] < yArr + hArr:
            equip_text_image = smallFont.render("100", True,
                                                values.COLOR_Yellow)
        else:
            equip_text_image = smallFont.render("100", True,
                                                values.COLOR_Purple)
        screen.blit(equip_text_image,
                    (xArr1 + wArr + sep + screen.get_width() * .055,
                     yArr + screen.get_height() * .0313))

    # Rotated form of the left arrow (Should probably change to a different sprite later)
    rightArr = pygame.transform.rotate(bigArr, 180)
    screen.blit(rightArr, (xArr1 + sep + sep + box + wArr, yArr))

    currentPreview = pygame.transform.scale(currentArray[startingDuck],
                                            (previewSize, previewSize))

    #TODO Preview of Duck in Current State
    if arrayIndex < 7:
        screen.blit(currentPreview,
                    (screen.get_width() / 3, screen.get_height() / 4))
    else:
        screen.blit(currentPreview,
                    (screen.get_width() / 2.625, screen.get_height() / 3.5))
    #will make these box objects for an array so we can move with arrows, know which ones have been purchased.
    if arrayIndex != 7:
        numboxes = 6
    else:
        numboxes = 3
    for i in range(numboxes):
        if arrayIndex == 7:
            # Make backgrounds in center of box
            pygame.draw.rect(
                screen, values.COLOR_Pink,
                ((i + 1) * screen.get_width() * .1157 -
                 screen.get_width() * .0289, screen.get_height() * .7610,
                 screen.get_width() * .0868, screen.get_width() * .0868), 0)
            screen.blit(
                currentArray[i],
                ((i + 1) * screen.get_width() * .1157 -
                 screen.get_width() * .0225, screen.get_height() * .77))
        else:
            pygame.draw.rect(
                screen, values.COLOR_Pink,
                ((i + 1) * screen.get_width() * .1157 -
                 screen.get_width() * .0289, screen.get_height() * .7610,
                 screen.get_width() * .0868, screen.get_width() * .0868), 0)
            screen.blit(
                currentArray[i],
                ((i + 1) * screen.get_width() * .1157 -
                 screen.get_width() * .0607, screen.get_height() * .7117))

    #4 boxes to change screen to purchase base skins, hats, trails, and backgrounds
    xCord = math.floor(screen.get_width() * .0289)
    yCord = math.floor(screen.get_height() * .1791)
    width = math.floor(screen.get_width() * .1591)
    height = math.floor(screen.get_height() * .0895)
    separation = math.floor(screen.get_height() * .0448)

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
    screen.blit(BS_text_image, (xCord + screen.get_width() * .0174,
                                yCord + screen.get_height() * .0313))

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
                (xCord + screen.get_width() * .0521, yCord +
                 screen.get_height() * .0313 + (height + separation) * 1))

    #Backgrounds Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord, yCord +
                      ((height + separation) * 2), width, height), 0)
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord + width and pygame.mouse.get_pos()[1] > (
            yCord +
        (height + separation) * 2) and pygame.mouse.get_pos()[1] < (
            yCord + height + (height + separation) * 2):
        Backgrounds_text_image = smallFont.render("Backgrounds", True,
                                                  values.COLOR_Yellow)
    else:
        Backgrounds_text_image = smallFont.render("Backgrounds", True,
                                                  values.COLOR_Purple)
    screen.blit(Backgrounds_text_image,
                (xCord + screen.get_width() * .0029, yCord +
                 screen.get_height() * .0313 + (height + separation) * 2))

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
                if homeCords[0] < pygame.mouse.get_pos()[0] < homeCords[0] + (
                        right - left - screen.get_width() *
                        .0231) / 3 and homeCords[1] < pygame.mouse.get_pos(
                        )[1] < homeCords[1] + screen.get_height() * .0448:
                    # return to home screen
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord < pygame.mouse.get_pos(
                )[1] < yCord + height:
                    noises.playSound("quack")
                    # Base skins box
                    startingArray = 0
                    #TODO make text red or highlight box, then switch screen to customize different asset
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (
                        height + separation) * 1 < pygame.mouse.get_pos(
                        )[1] < yCord + height + (height + separation) * 1:
                    noises.playSound("quack")
                    # Accessories box
                    startingArray = startingDuck + 1
                    #TODO make text red or highlight box, then switch screen to customize different asset
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (
                        height + separation) * 2 < pygame.mouse.get_pos(
                        )[1] < yCord + height + (height + separation) * 2:
                    noises.playSound("quack")
                    # Backgrounds box
                    startingArray = 7
                    startingDuck = 0
                    #TODO make text red or highlight box, then switch screen to customize different asset

                    #click on left arrow, move boxes to the left
                elif xArr1 < pygame.mouse.get_pos(
                )[0] < xArr1 + wArr and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    noises.playSound("quack")
                    startingDuck -= 1
                    if startingDuck < 0:
                        if arrayIndex < 7:
                            startingDuck = len(allSkins) - 1
                        else:
                            startingDuck = 2
                    # Make the duck the new duck
                    currentPreview = pygame.transform.scale(
                        currentArray[startingDuck], (previewSize, previewSize))

                    #click on equip or buy
                elif xArr1 + sep + wArr < pygame.mouse.get_pos(
                )[0] < xArr1 + sep + wArr + box and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    # Check to see if they have the coins to buy the skin then unlock and select it
                    noises.playSound("quack")
                    # Set the duck to the current one with values.py
                    # Figure out which array we are currently in
                    if usedArray[startingDuck] in ownedSkins or usedArray[
                            startingDuck] in ownedBackgrounds:
                        # We own the item, figure out what it is
                        if "background" in usedArray[startingDuck]:
                            values.setBackground(usedArray[startingDuck])
                        else:
                            values.setSkin(usedArray[startingDuck])
                    else:
                        if coins_imported >= 100:
                            # Can purchase
                            if "background" in usedArray[startingDuck]:
                                # It is a background
                                customizationIO.backgrounds.append(
                                    usedArray[startingDuck])
                                customizationIO.current_background = startingDuck
                            else:
                                # It is a skin
                                customizationIO.skins.append(
                                    usedArray[startingDuck])
                                customizationIO.current_skin = arrayIndex
                                customizationIO.current_hat = startingDuck
                            coins_imported -= 100
                            customizationIO.coins = coins_imported
                            customizationIO.save_customization()
                            customizationIO.load_customization()
                            ownedSkins = customizationIO.skins
                            ownedBackgrounds = customizationIO.backgrounds

                    #click on right arrow, move boxes to the right
                elif xArr1 + sep + wArr + box + sep < pygame.mouse.get_pos(
                )[0] < xArr1 + sep + sep + wArr + box + wArr and yArr < pygame.mouse.get_pos(
                )[1] < yArr + hArr:
                    noises.playSound("quack")
                    startingDuck += 1
                    if arrayIndex < 7:
                        if startingDuck > len(allSkins) - 1:
                            startingDuck = 0
                    else:
                        if startingDuck > 2:
                            startingDuck = 0
                    # Make the duck the new duck
                    currentPreview = pygame.transform.scale(
                        currentArray[startingDuck], (previewSize, previewSize))

        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.HOME)
                main.main()

    return startingDuck, startingArray
