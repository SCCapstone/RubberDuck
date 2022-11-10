import pygame
import json
from assets import values
import menuStructure as menuS
import os
#from fileio import settingIO


def StartLoad():
    # TODO
    pass


def saveStats():
    # TODO
    pass


def settingScreen(noises):
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join(
            "assets",
            "backgrounds",
            "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background,
        (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Draw Big Box tall and normal width
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    botLeft = screen.get_height() / 16
    topRight = screen.get_height() / 16 * 15
    pygame.draw.rect(
        screen,
        values.COLOR_Pink,
        (left,
         botLeft,
         right -
         left,
         topRight -
         botLeft),
        0)

    # Title at top of box centered
    titleFont = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .03))
    title_text_image = titleFont.render(
        "Settings", True, values.COLOR_Purple)
    title_rect = title_text_image.get_rect(
        center=(
            screen.get_width() / 2,
            screen.get_height() / 16 * 2))
    screen.blit(title_text_image, title_rect)

    subtitleFont = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .017))

    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3
    
    # Add 2 cenered buttons
    importCords = (left + ((right - left) / 2) - widthButton-10 , screen.get_height() / 16 * 12)
    exportCords = (left + ((right - left) / 2) + 10, screen.get_height() / 16 * 12)
    
    pygame.draw.rect(screen, values.COLOR_Purple, (importCords[0], importCords[1], widthButton, 50), 0)
    pygame.draw.rect(screen, values.COLOR_Purple, (exportCords[0], exportCords[1], widthButton, 50), 0)
    
    #import_settings_text_image = subtitleFont.render("Import Settings", True, values.COLOR_Pink)
    #export_settings_text_image = subtitleFont.render("Export Settings", True, values.COLOR_Pink)
    
    #screen.blit(import_settings_text_image, (importCords[0], importCords[1]))
    #screen.blit(export_settings_text_image, (exportCords[0], exportCords[1]))
    
    homeCords = (left + 10, screen.get_height() / 16 * 13.5)
    defaultCords = (
        10 +
        homeCords[0] +
        widthButton,
        screen.get_height() /
        16 *
        13.5)
    quitCoords = (
        10 +
        defaultCords[0] +
        widthButton,
        screen.get_height() /
        16 *
        13.5)

    # Draw Rects for buttons
    pygame.draw.rect(
        screen,
        values.COLOR_Purple,
        (homeCords[0],
         homeCords[1],
         widthButton,
         50))
    pygame.draw.rect(
        screen,
        values.COLOR_Purple,
        (defaultCords[0],
         defaultCords[1],
         widthButton,
         50))
    pygame.draw.rect(
        screen,
        values.COLOR_Purple,
        (quitCoords[0],
         quitCoords[1],
         widthButton,
         50))

    # Add text to center of buttons
    default_text_image = subtitleFont.render(
        "Default", True, values.COLOR_Pink)
    home_text_image = subtitleFont.render("Home", True, values.COLOR_Pink)
    quit_text_image = subtitleFont.render("Quit", True, values.COLOR_Pink)

    screen.blit(
        home_text_image,
        (homeCords[0] +
         widthButton /
         2 -
         home_text_image.get_width() /
         2,
         homeCords[1] +
         25 -
         home_text_image.get_height() /
         2))
    screen.blit(
        default_text_image,
        (defaultCords[0] +
         widthButton /
         2 -
         default_text_image.get_width() /
         2,
         defaultCords[1] +
         25 -
         default_text_image.get_height() /
         2))
    screen.blit(
        quit_text_image,
        (quitCoords[0] +
         widthButton /
         2 -
         quit_text_image.get_width() /
         2,
         quitCoords[1] +
         25 -
         quit_text_image.get_height() /
         2))

    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # check if mouse is in rect
                if homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + widthButton and homeCords[1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # share stats
                    noises.playSound("quack")
                    menuS.setGameMenu(menuS.Menu.HOME)
                elif defaultCords[0] < pygame.mouse.get_pos()[0] < defaultCords[0] + widthButton and defaultCords[1] < pygame.mouse.get_pos()[1] < defaultCords[1] + 50:
                    # go to home screeni
                    noises.playSound("quack")
                    pass
                elif quitCoords[0] < pygame.mouse.get_pos()[0] < quitCoords[0] + widthButton and quitCoords[1] < pygame.mouse.get_pos()[1] < quitCoords[1] + 50:
                    # quit game
                    noises.playSound("quack")
                    menuS.setGameMenu(menuS.Menu.QUIT)
        elif event.type == pygame.QUIT:
            menuS.setGameMenu(menuS.Menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.setGameMenu(menuS.Menu.QUIT)
