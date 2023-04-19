import os
import sys

sys.path.append('..')
#import pytest_bdd methods and feature file for this test
from pytest_bdd import *
import pygame

import menuStructure as menuS
from fileio import settingIO
from views import settingScreen as settingsS
from assets import values

global pass_variable


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Name')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the name')
def test_change_name():
    settingIO.Player_Name = "test"
    # Cant test colliding with the name box because it is not a sprite
    # and cant be added to a group


@then('the players name is changed')
def test_name_changed():
    assert settingIO.get_username() == "test"


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Master Volume')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the master volume')
def test_change_master_volume():
    global pass_variable
    left = 100
    factor = 20
    image = pygame.Surface((50, 50))
    screen = pygame.Surface((500, 500))
    range = 200
    height = 5
    pygame.mouse.set_pos((left + factor + image.get_width() + range / 2,
                          screen.get_height() / 16 * height + 25))
    pass_variable = settingsS.checkSliderCords(left, factor, image, screen,
                                               range, height)


@then('the players master volume is changed')
def test_master_volume_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Music Volume')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the music volume')
def test_change_music_volume():
    global pass_variable
    left = 100
    factor = 20
    image = pygame.Surface((50, 50))
    screen = pygame.Surface((500, 500))
    range = 200
    height = 6
    pygame.mouse.set_pos((left + factor + image.get_width() + range / 2,
                          screen.get_height() / 16 * height + 25))
    pass_variable = settingsS.checkSliderCords(left, factor, image, screen,
                                               range, height)


@then('the players music volume is changed')
def test_music_volume_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change SFX Volume')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the SFX volume')
def test_change_sfx_volume():
    global pass_variable
    left = 100
    factor = 20
    image = pygame.Surface((50, 50))
    screen = pygame.Surface((500, 500))
    range = 200
    height = 7
    pygame.mouse.set_pos((left + factor + image.get_width() + range / 2,
                          screen.get_height() / 16 * height + 25))
    pass_variable = settingsS.checkSliderCords(left, factor, image, screen,
                                               range, height)


@then('the players SFX volume is changed')
def test_sfx_volume_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Difficulty Easy')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the difficulty to easy')
def test_change_difficulty_easy():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3

    easydifficultySettingCords = (left + 30 + widthButton,
                                  screen.get_height() / 16 * 7)
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .019))
    easy_image = subtitleFont.render("Easy", True, values.COLOR_Red)
    mouse_cords = (easydifficultySettingCords[0] + 1,
                   easydifficultySettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkDifCords(easydifficultySettingCords,
                                            easy_image)


@then('the players difficulty is changed to easy')
def test_difficulty_easy_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Difficulty Medium')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the difficulty to medium')
def test_change_difficulty_medium():
    global pass_variable
    screen = pygame.Surface((500, 500))
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .019))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    easy_image = subtitleFont.render("Easy", True, values.COLOR_Red)
    easy_image_width = easy_image.get_width()
    dash_image = subtitleFont.render("/", True, values.COLOR_Purple)
    dash_width = dash_image.get_width()
    mediumdifficultySettingCords = (left + 30 + widthButton +
                                    easy_image_width + 10 + dash_width + 10,
                                    screen.get_height() / 16 * 7)
    medium_image = subtitleFont.render("Medium", True, values.COLOR_Red)
    mouse_cords = (mediumdifficultySettingCords[0] + 1,
                   mediumdifficultySettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkDifCords(mediumdifficultySettingCords,
                                            medium_image)


@then('the players difficulty is changed to medium')
def test_difficulty_medium_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Difficulty Hard')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the difficulty to hard')
def test_change_difficulty_hard():
    global pass_variable
    screen = pygame.Surface((500, 500))
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .019))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    easy_image = subtitleFont.render("Easy", True, values.COLOR_Red)
    easy_image_width = easy_image.get_width()
    medium_image = subtitleFont.render("Medium", True, values.COLOR_Red)
    medium_image_width = medium_image.get_width()
    dash_image = subtitleFont.render("/", True, values.COLOR_Purple)
    dash_width = dash_image.get_width()
    harddifficultySettingCords = (left + 30 + widthButton + easy_image_width +
                                  10 + dash_width + 10 +
                                  medium_image_width + 10 + dash_width + 10,
                                  screen.get_height() / 16 * 7)
    hard_image = subtitleFont.render("Hard", True, values.COLOR_Red)
    mouse_cords = (harddifficultySettingCords[0] + 1,
                   harddifficultySettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkDifCords(harddifficultySettingCords,
                                            hard_image)


@then('the players difficulty is changed to hard')
def test_difficulty_hard_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Input Wasd')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the input to wasd')
def test_change_input_wasd():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3

    wasdSettingCords = (left + 30 + widthButton, screen.get_height() / 16 * 9)
    mouse_cords = (wasdSettingCords[0] + 1, wasdSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(wasdSettingCords, 150)


@then('the players input is changed to wasd')
def test_input_wasd_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Change Input Arrows')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player changes the input to arrows')
def test_change_input_arrows():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3

    arrowsSettingCords = (left + 30 + widthButton,
                          screen.get_height() / 16 * 11)
    mouse_cords = (arrowsSettingCords[0] + 1, arrowsSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(arrowsSettingCords, 150)


@then('the players input is changed to arrows')
def test_input_arrows_changed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Help Button')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player clicks the help button')
def test_click_help_button():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    helpSettingCords = (left + 30 + widthButton, screen.get_height() / 16 * 13)
    mouse_cords = (helpSettingCords[0] + 1, helpSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(helpSettingCords, widthButton)


@then('the help popup is displayed')
def test_help_screen_displayed():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Default Button')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player clicks the default button')
def test_click_default_button():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    defaultSettingCords = (left + 30 + widthButton,
                           screen.get_height() / 16 * 15)
    mouse_cords = (defaultSettingCords[0] + 1, defaultSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(defaultSettingCords, widthButton)


@then('the settings are reset to default')
def test_settings_set_to_default():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Export Button')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player clicks the export button')
def test_click_export_button():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    exportSettingCords = (left + 30 + widthButton,
                          screen.get_height() / 16 * 17)
    mouse_cords = (exportSettingCords[0] + 1, exportSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(exportSettingCords, widthButton)


@then('the settings are exported to a file')
def test_settings_exported():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################


@scenario('../test/features/settingsScreen.feature',
          'Setting Screen - Import Button')
@given('the player is on the settings screen')
def test_settings_Screen():
    pygame.init()
    # Make game full screen
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ducks In Space")
    pygame.display.update()
    menuS.set_game_menu(menuS.menu.SETTING)
    settingIO.load_settings(values.SETTING_PATH)


@when('the player clicks the import button')
def test_click_import_button():
    global pass_variable
    screen = pygame.Surface((500, 500))
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    widthButton = (right - left - 40) / 3
    importSettingCords = (left + 30 + widthButton,
                          screen.get_height() / 16 * 19)
    mouse_cords = (importSettingCords[0] + 1, importSettingCords[1] + 1)
    pygame.mouse.set_pos(mouse_cords)
    pass_variable = settingsS.checkCords(importSettingCords, widthButton)


@then('the settings are imported from a file')
def test_settings_imported():
    global pass_variable
    assert pass_variable == True
    pass_variable = None


############################################################################################################
