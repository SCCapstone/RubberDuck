""" summary: Class to run Settings Screen
"""
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import settingIO

#from fileio import settingIO
global active
active = False


def settings_screen(noises):
    global active
    """summay: running method for screen (loop)

    Args:
        noises (SFXHandler): sounds handler for screen
    """

    screen, left, right, subtitleFont, titleFont = draw_background()

    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3

    # Player Name Section
    player_name_image = subtitleFont.render("Player Name:", True,
                                            values.COLOR_Purple)
    playerCords = (left + 10, screen.get_height() / 16 * 3)
    screen.blit(player_name_image, playerCords)

    # Text box for player name right of player name
    inputNameBox = pygame.Rect(left + 10 + player_name_image.get_width(),
                               screen.get_height() / 16 * 3, widthButton, 50)
    pygame.draw.rect(screen, values.COLOR_Purple, inputNameBox, 0)
    #Write player name in box

    if active:
        #Add blinking cursor
        player_name_value_image = subtitleFont.render(
            settingIO.Player_Name + "|", True, values.COLOR_White)
        # flicker every 500 ms
        if pygame.time.get_ticks() % 1000 > 500:
            player_name_value_image = subtitleFont.render(
                settingIO.Player_Name, True, values.COLOR_White)
    else:
        player_name_value_image = subtitleFont.render(settingIO.Player_Name,
                                                      True, values.COLOR_White)
    screen.blit(player_name_value_image,
                (inputNameBox.x + 5, inputNameBox.y + 5))

    playerValueCords = (left + 10 + player_name_image.get_width() + 5,
                        screen.get_height() / 16 * 3 + 5)
    screen.blit(player_name_value_image, playerValueCords)

    # Master Volume Slider
    master_volume_image = subtitleFont.render("Master Volume:", True,
                                              values.COLOR_Purple)
    masterVolCords = (left + 10, screen.get_height() / 16 * 4)
    screen.blit(master_volume_image, masterVolCords)

    masterValRange = right - left - 40 - master_volume_image.get_width()
    # curved rectangle for volume slider inline with text
    pygame.draw.rect(
        screen, values.COLOR_Purple,
        (left + 30 + master_volume_image.get_width(),
         screen.get_height() / 16 * 3.95 + 20, masterValRange, 10), 0)
    # volume slider
    pygame.draw.rect(screen, values.COLOR_Red,
                     (left + 30 + master_volume_image.get_width(),
                      screen.get_height() / 16 * 3.95 + 20,
                      masterValRange * settingIO.Master_Volume / 100, 10), 0)

    # Music Volume Slider
    music_volume_image = subtitleFont.render("Music Volume:", True,
                                             values.COLOR_Purple)
    musicVolCords = (left + 50, screen.get_height() / 16 * 5)
    screen.blit(music_volume_image, musicVolCords)

    musicValRange = right - left - 80 - music_volume_image.get_width()
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (left + 70 + music_volume_image.get_width(),
                      screen.get_height() / 16 * 4.95 + 20, musicValRange, 10),
                     0)
    pygame.draw.rect(screen, values.COLOR_Red,
                     (left + 70 + music_volume_image.get_width(),
                      screen.get_height() / 16 * 4.95 + 20,
                      musicValRange * settingIO.Music_Volume / 100, 10), 0)

    # SFX Volume Slider
    sfx_volume_image = subtitleFont.render("SFX Volume:", True,
                                           values.COLOR_Purple)
    sfxVolCords = (left + 50, screen.get_height() / 16 * 6)
    screen.blit(sfx_volume_image, sfxVolCords)

    sfxValRange = right - left - 80 - sfx_volume_image.get_width()
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (left + 70 + sfx_volume_image.get_width(),
                      screen.get_height() / 16 * 5.95 + 20, sfxValRange, 10),
                     0)
    pygame.draw.rect(screen, values.COLOR_Red,
                     (left + 70 + sfx_volume_image.get_width(),
                      screen.get_height() / 16 * 5.95 + 20,
                      sfxValRange * settingIO.SFX_Volume / 100, 10), 0)

    # Difficulty Selector Heading
    difficulty_image = subtitleFont.render("Difficulty:", True,
                                           values.COLOR_Purple)
    difficultyCords = (left + 10, screen.get_height() / 16 * 7)
    screen.blit(difficulty_image, difficultyCords)

    # TODO - Add special coloring for current difficulty (new color or just yellow?)
    # Difficulty Settings
    # Easy setting
    easydifficultySettingCords = (left + 30 + widthButton,
                                  screen.get_height() / 16 * 7)
    # Highlighting Easy
    if settingIO.Difficulty == "Easy":
        easy_difficulty_settings_image = subtitleFont.render(
            "Easy", True, values.COLOR_Red)
    elif pygame.mouse.get_pos(
    )[0] > easydifficultySettingCords[0] and pygame.mouse.get_pos(
    )[0] < easydifficultySettingCords[0] + 120 and pygame.mouse.get_pos(
    )[1] > easydifficultySettingCords[1] and pygame.mouse.get_pos(
    )[1] < easydifficultySettingCords[1] + 30:
        easy_difficulty_settings_image = subtitleFont.render(
            "Easy", True, values.COLOR_Yellow)
    else:
        easy_difficulty_settings_image = subtitleFont.render(
            "Easy", True, values.COLOR_Purple)
    screen.blit(easy_difficulty_settings_image, easydifficultySettingCords)
    # Slash after Easy
    slash_one_image = subtitleFont.render("/", True, values.COLOR_Purple)
    slashOneCords = (easydifficultySettingCords[0] + 120,
                     screen.get_height() / 16 * 7)
    screen.blit(slash_one_image, slashOneCords)
    # Medium setting
    mediumdifficultySettingCords = (slashOneCords[0] + 20,
                                    screen.get_height() / 16 * 7)
    # Highlighting Medium
    if settingIO.Difficulty == "Medium":
        medium_difficulty_settings_image = subtitleFont.render(
            "Medium", True, values.COLOR_Red)
    elif pygame.mouse.get_pos(
    )[0] > mediumdifficultySettingCords[0] and pygame.mouse.get_pos(
    )[0] < mediumdifficultySettingCords[0] + 180 and pygame.mouse.get_pos(
    )[1] > mediumdifficultySettingCords[1] and pygame.mouse.get_pos(
    )[1] < mediumdifficultySettingCords[1] + 30:
        medium_difficulty_settings_image = subtitleFont.render(
            "Medium", True, values.COLOR_Yellow)
    else:
        medium_difficulty_settings_image = subtitleFont.render(
            "Medium", True, values.COLOR_Purple)
    screen.blit(medium_difficulty_settings_image, mediumdifficultySettingCords)
    # Slash after Medium
    slash_two_image = subtitleFont.render("/", True, values.COLOR_Purple)
    slashTwoCords = (mediumdifficultySettingCords[0] + 180,
                     screen.get_height() / 16 * 7)
    screen.blit(slash_two_image, slashTwoCords)
    # Hard setting
    harddifficultySettingCords = (slashTwoCords[0] + 20,
                                  screen.get_height() / 16 * 7)
    # Highlighting Hard
    if settingIO.Difficulty == "Hard":
        hard_difficulty_settings_image = subtitleFont.render(
            "Hard", True, values.COLOR_Red)
    elif pygame.mouse.get_pos(
    )[0] > harddifficultySettingCords[0] and pygame.mouse.get_pos(
    )[0] < harddifficultySettingCords[0] + 120 and pygame.mouse.get_pos(
    )[1] > harddifficultySettingCords[1] and pygame.mouse.get_pos(
    )[1] < harddifficultySettingCords[1] + 30:
        hard_difficulty_settings_image = subtitleFont.render(
            "Hard", True, values.COLOR_Yellow)
    else:
        hard_difficulty_settings_image = subtitleFont.render(
            "Hard", True, values.COLOR_Purple)
    screen.blit(hard_difficulty_settings_image, harddifficultySettingCords)

    # Coordinates for back button
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos()[0] > homeCords[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * .122 and pygame.mouse.get_pos(
    )[1] > homeCords[1] and pygame.mouse.get_pos()[1] < values.screenY * .06:
        SR_text_image = titleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = titleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))

    # Add 2 centered buttons
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
    defaultCords = (left + 20 + widthButton, screen.get_height() / 16 * 12)

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
        settingIO.save_settings()
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:

                # check if mouse is in rect
                if checkCords(homeCords, widthButton):
                    # share stats
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif checkCords(defaultCords, widthButton):
                    noises.playSound("quack")
                    settingIO.load_default_settings()
                elif checkCords(importCords, widthButton):
                    noises.playSound("quack")
                    settingIO.import_settings()
                elif checkCords(exportCords, widthButton):
                    noises.playSound("quack")
                    settingIO.export_settings()
                elif checkDifCords(easydifficultySettingCords, 120):
                    noises.playSound("quack")
                    settingIO.Difficulty = "Easy"
                elif checkDifCords(mediumdifficultySettingCords, 180):
                    noises.playSound("quack")
                    settingIO.Difficulty = "Medium"
                elif checkDifCords(harddifficultySettingCords, 120):
                    noises.playSound("quack")
                    settingIO.Difficulty = "Hard"
                elif checkSliderCords(left, 30, master_volume_image, screen,
                                      masterValRange, 3.95):
                    noises.playSound("quack")
                    newPercent = round_Percent(
                        (pygame.mouse.get_pos()[0] -
                         (left + 30 + master_volume_image.get_width())) /
                        masterValRange * 100)
                    settingIO.Master_Volume = newPercent
                elif checkSliderCords(left, 70, music_volume_image, screen,
                                      musicValRange, 4.95):
                    noises.playSound("quack")
                    newPercent = round_Percent(
                        (pygame.mouse.get_pos()[0] -
                         (left + 70 + music_volume_image.get_width())) /
                        musicValRange * 100)
                    settingIO.Music_Volume = newPercent
                    noises.music_volume(settingIO.Music_Volume)
                elif checkSliderCords(left, 70, sfx_volume_image, screen,
                                      sfxValRange, 5.95):
                    noises.playSound("quack")
                    newPercent = round_Percent(
                        (pygame.mouse.get_pos()[0] -
                         (left + 70 + sfx_volume_image.get_width())) /
                        sfxValRange * 100)
                    settingIO.SFX_Volume = newPercent

                if inputNameBox.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False

        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)
            if active:
                if event.key == pygame.K_BACKSPACE:
                    settingIO.Player_Name = settingIO.Player_Name[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    if (len(settingIO.Player_Name) < 8):
                        settingIO.Player_Name += event.unicode
                settingIO.save_settings()


def round_Percent(percent):
    """Round percent to nearest 5 up if above 50, down if below 50

    Args:
        percent (float): raw percent

    Returns:
        int: rounded percent to nearest 5
    """
    if percent < 50:
        return percent - (percent % 5)
    else:
        return percent + (5 - percent % 5)


def draw_background():
    """summary: draw background image
    """
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
    return screen, left, right, subtitleFont, titleFont


def checkCords(cords, width):
    """summary: Checks if cordinated were clicke

    Args:
        cords (tuple[float,float]): cordinates of button being checked
        width (float): width of a button

    Returns:
        boolean: true if clicked, false if not
    """
    return cords[0] < pygame.mouse.get_pos()[0] < cords[0] + width and cords[
        1] < pygame.mouse.get_pos()[1] < cords[1] + 50


def checkDifCords(cords, factor):
    """summary: Checks if cordinated were clicke

    Args:
        cords (tuple[float,float]): cordinates of button being checked
        factor (float): width of a button

    Returns:
        boolean: true if clicked, false if not
    """
    return cords[0] < pygame.mouse.get_pos()[0] < cords[0] + factor and cords[
        1] < pygame.mouse.get_pos()[1] < cords[1] + 30


def checkSliderCords(left, factor, image, screen, range, height):
    """summary: Checks if slider was clicked

    Args:
        left (float): left side of slider
        factor (float): factor of slider
        image (pygame.image): image of slider
        screen (pygame.display): screen
        range (float): range of slider
        height (float): height of slider

    Returns:
        boolean: true if clicked, false if not
    """
    return left + factor + image.get_width() < pygame.mouse.get_pos(
    )[0] < left + factor + image.get_width() + range and screen.get_height(
    ) / 16 * height + 20 < pygame.mouse.get_pos(
    )[1] < screen.get_height() / 16 * height + 30
