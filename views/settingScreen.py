#Imports
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import settingIO

#from fileio import settingIO


# TODO - Add a way to load the settings
def load_settings():
    pass


# TODO - Add a way to save the settings
def save_settings():
    # TODO
    pass


# Runs the settings screen
def settings_screen(noises):
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Draw Big Box tall and normal width
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    botLeft = screen.get_height() / 16
    topRight = screen.get_height() / 16 * 15
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (left, botLeft, right - left, topRight - botLeft), 0)

    # Title at top of box centered
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))
    title_text_image = titleFont.render("Settings", True, values.COLOR_Purple)
    title_rect = title_text_image.get_rect(center=(screen.get_width() / 2,
                                                   screen.get_height() / 16 *
                                                   2))
    screen.blit(title_text_image, title_rect)

    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .019))

    # Coordinates for back button
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos(
    )[0] > values.screenX * .0065 and pygame.mouse.get_pos(
    )[0] < values.screenX * .09 and pygame.mouse.get_pos(
    )[1] > values.screenY * .011 and pygame.mouse.get_pos(
    )[1] < values.screenY * .05:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))

    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3

    # Add 2 cenered buttons
    importCords = (left + ((right - left) / 2) - widthButton - 10,
                   screen.get_height() / 16 * 13.5)
    exportCords = (left + ((right - left) / 2) + 10,
                   screen.get_height() / 16 * 13.5)

    # Draw the buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (importCords[0], importCords[1], widthButton, 50), 0)
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (exportCords[0], exportCords[1], widthButton, 50), 0)

    import_settings_text_image = subtitleFont.render("Import", True,
                                                     values.COLOR_Pink)
    export_settings_text_image = subtitleFont.render("Export", True,
                                                     values.COLOR_Pink)

    # Draw the text on the buttons in the center
    import_settings_rect = import_settings_text_image.get_rect(
        center=(importCords[0] + widthButton / 2, importCords[1] + 25))
    export_settings_rect = export_settings_text_image.get_rect(
        center=(exportCords[0] + widthButton / 2, exportCords[1] + 25))

    screen.blit(import_settings_text_image, import_settings_rect)
    screen.blit(export_settings_text_image, export_settings_rect)

    # Make cords for 3 inline buttons
    defaultCords = (left + 10 + widthButton,
                    screen.get_height() / 16 * 12)

    # Draw Rects for buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (defaultCords[0], defaultCords[1], widthButton, 50))

    # Add text to center of buttons
    default_text_image = subtitleFont.render("Default", True,
                                             values.COLOR_Pink)

    # Add text to screen
    screen.blit(default_text_image,
                (defaultCords[0] + widthButton / 2 -
                 default_text_image.get_width() / 2,
                 defaultCords[1] + 25 - default_text_image.get_height() / 2))

    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                if homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + widthButton and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # share stats
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif defaultCords[0] < pygame.mouse.get_pos(
                )[0] < defaultCords[0] + widthButton and defaultCords[
                        1] < pygame.mouse.get_pos()[1] < defaultCords[1] + 50:
                    # go to home screeni
                    noises.playSound("quack")
                elif importCords[0] < pygame.mouse.get_pos(
                )[0] < importCords[0] + widthButton and importCords[
                        1] < pygame.mouse.get_pos()[1] < importCords[1] + 50:
                    noises.playSound("quack")
                    settingIO.import_settings()
                elif exportCords[0] < pygame.mouse.get_pos(
                )[0] < exportCords[0] + widthButton and exportCords[
                        1] < pygame.mouse.get_pos()[1] < exportCords[1] + 50:
                    noises.playSound("quack")
                    settingIO.export_settings()
        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)
