""" summary: Class to run Settings Screen
"""
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import settingIO
from views import gameScreen
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

    ## put easy, medium, hard text after difficulty_image
    easydifficultySettingCords = (left + 30 + widthButton,
                                  screen.get_height() / 16 * 7)
    #for image size
    easy_image = subtitleFont.render("Easy", True, values.COLOR_Red)
    #find width of image
    easy_image_width = easy_image.get_width()
    if settingIO.DifficultyLevel is settingIO.difficulty.EASY:
        pass
    elif checkDifCords(easydifficultySettingCords, easy_image):
        easy_image = subtitleFont.render("Easy", True, values.COLOR_Yellow)
    else:
        easy_image = subtitleFont.render("Easy", True, values.COLOR_Purple)
    screen.blit(easy_image, easydifficultySettingCords)

    # Dash between easy and medium
    dash_image = subtitleFont.render("/", True, values.COLOR_Purple)
    dash_width = dash_image.get_width()
    dashCords = (left + 30 + widthButton + easy_image_width + 10,
                 screen.get_height() / 16 * 7)
    screen.blit(dash_image, dashCords)

    # Put to right of easy
    mediumdifficultySettingCords = (left + 30 + widthButton +
                                    easy_image_width + 10 + dash_width + 10,
                                    screen.get_height() / 16 * 7)
    medium_image = subtitleFont.render("Medium", True, values.COLOR_Red)
    medium_image_width = medium_image.get_width()
    if settingIO.DifficultyLevel is settingIO.difficulty.MEDIUM:
        pass
    elif checkDifCords(mediumdifficultySettingCords, medium_image):
        medium_image = subtitleFont.render("Medium", True, values.COLOR_Yellow)
    else:
        medium_image = subtitleFont.render("Medium", True, values.COLOR_Purple)
    screen.blit(medium_image, mediumdifficultySettingCords)

    dash_image2 = subtitleFont.render("/", True, values.COLOR_Purple)
    dashCords2 = (left + 30 + widthButton + easy_image_width +
                  10 + dash_width + 10 + medium_image_width + 10,
                  screen.get_height() / 16 * 7)
    screen.blit(dash_image2, dashCords2)

    # Put to right of medium
    harddifficultySettingCords = (left + 30 + widthButton + easy_image_width +
                                  10 + dash_width + 10 +
                                  medium_image_width + 10 + dash_width + 10,
                                  screen.get_height() / 16 * 7)
    hard_image = subtitleFont.render("Hard", True, values.COLOR_Red)
    if settingIO.DifficultyLevel is settingIO.difficulty.HARD:
        pass
    elif checkDifCords(harddifficultySettingCords, hard_image):
        hard_image = subtitleFont.render("Hard", True, values.COLOR_Yellow)
    else:
        hard_image = subtitleFont.render("Hard", True, values.COLOR_Purple)
    screen.blit(hard_image, harddifficultySettingCords)
    
    #KeyMapping
    key_image = subtitleFont.render("Key Mapping:", True,
                                            values.COLOR_Purple)
    key_Cords = (left + 10, screen.get_height() / 16 * 8)
    screen.blit(key_image, key_Cords)

    # AWSD setting
    awsd_Cords = (left + 60 + widthButton,
                                   screen.get_height() / 16 * 8)
    # Highlighting AWSD
    #if settingIO.Keymap_Left == pygame.K_a:
    if gameScreen.LEFT == pygame.K_a:
        awsd_image = subtitleFont.render(
            "AWSD", True, values.COLOR_Red)
    elif pygame.mouse.get_pos(
     )[0] > awsd_Cords[0] and pygame.mouse.get_pos(
     )[0] < awsd_Cords[0] + 150 and pygame.mouse.get_pos(
     )[1] > awsd_Cords[1] and pygame.mouse.get_pos(
     )[1] < awsd_Cords[1] + 30:
         awsd_image = subtitleFont.render(
             "AWSD", True, values.COLOR_Yellow)
         awsd_image = subtitleFont.render(
             "AWSD", True, values.COLOR_Purple)
    screen.blit(awsd_image, awsd_Cords)
     # Slash after AWSD
    slash_awsd_image = subtitleFont.render("/", True, values.COLOR_Purple)
    slashAWSD = (awsd_Cords[0] + 150,
                      screen.get_height() / 16 * 8)
    screen.blit(slash_awsd_image, slashAWSD)
     # Arrow keys setting
    arrow_Cords = (slashAWSD[0] + 20,
                                     screen.get_height() / 16 * 8)
     # Highlighting Arrow Keys
     #if settingIO.Keymap_Left == pygame.K_LEFT:
    if gameScreen.LEFT == pygame.K_LEFT:
         arrows_image = subtitleFont.render(
             "Arrow Keys", True, values.COLOR_Red)
    elif pygame.mouse.get_pos(
     )[0] > arrow_Cords[0] and pygame.mouse.get_pos(
     )[0] < arrow_Cords[0] + 300 and pygame.mouse.get_pos(
     )[1] > arrow_Cords[1] and pygame.mouse.get_pos(
     )[1] < arrow_Cords[1] + 30:
         arrows_image = subtitleFont.render(
             "Arrow Keys", True, values.COLOR_Yellow)
    else:
         arrows_image = subtitleFont.render(
             "Arrow Keys", True, values.COLOR_Purple)
    screen.blit(arrows_image, arrow_Cords)

    # Coordinates for back button
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos()[0] > homeCords[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * .122 and pygame.mouse.get_pos(
    )[1] > homeCords[1] and pygame.mouse.get_pos()[1] < values.screenY * .06:
        SR_text_image = titleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = titleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))

    homeBox = pygame.Rect(homeCords[0],
                          homeCords[1], SR_text_image.get_width(),
                          SR_text_image.get_height())

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
                if homeBox.collidepoint(pygame.mouse.get_pos()):
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
                elif checkDifCords(easydifficultySettingCords, easy_image):
                    noises.playSound("quack")
                    settingIO.DifficultyLevel = settingIO.difficulty.EASY
                elif checkDifCords(mediumdifficultySettingCords, medium_image):
                    noises.playSound("quack")
                    settingIO.DifficultyLevel = settingIO.difficulty.MEDIUM
                elif checkDifCords(harddifficultySettingCords, hard_image):
                    noises.playSound("quack")
                    settingIO.DifficultyLevel = settingIO.difficulty.HARD
                #key mapping (NOT WORKING YET)
                elif checkCords(awsd_Cords, 150):
                     noises.playSound("quack")
                    #settingIO.KeyMap_Left = pygame.K_a
                     #settingIO.KeyMap_Right = pygame.K_d
                     #settingIO.KeyMap_Up = pygame.K_w
                     #settingIO.KeyMap_Down = pygame.K_s
                     gameScreen.LEFT = pygame.K_a
                     gameScreen.RIGHT = pygame.K_d
                     gameScreen.UP = pygame.K_w
                     gameScreen.DOWN = pygame.K_s
                 #key mapping (NOT WORKING YET)
                elif checkCords(arrow_Cords, 300):
                     noises.playSound("quack")
                elif checkSliderCords(left, 30, master_volume_image, screen,
                                      masterValRange, 3.95):
                    noises.playSound("quack")
                    #settingIO.KeyMap_Left = pygame.K_LEFT
                    #settingIO.KeyMap_Right = pygame.K_RIGHT
                    #settingIO.KeyMap_Up = pygame.K_UP
                    #settingIO.KeyMap_Down = pygame.K_DOWN
                    gameScreen.LEFT = pygame.K_LEFT
                    gameScreen.RIGHT = pygame.K_RIGHT
                    gameScreen.UP = pygame.K_UP
                    gameScreen.DOWN = pygame.K_DOWN
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


def checkDifCords(cords, image):
    """summary: Checks if cordinated were clicke

    Args:
        cords (tuple[float,float]): cordinates of button being checked
        factor (float): width of a button

    Returns:
        boolean: true if clicked, false if not
    """
    return pygame.mouse.get_pos()[0] > cords[0] and pygame.mouse.get_pos(
    )[0] < cords[0] + image.get_width() and pygame.mouse.get_pos()[1] > cords[
        1] and pygame.mouse.get_pos()[1] < cords[1] + image.get_height()


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
