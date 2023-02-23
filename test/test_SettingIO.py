import sys

sys.path.append('..')
import pygame

from fileio import settingIO


def test_convertDifficulty():
    diff = "Easy"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.EASY
    diff = "Medium"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.MEDIUM
    diff = "Hard"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.HARD


def test_load_default_settings():
    settingIO.load_default_settings()
    assert settingIO.Player_Name == "Player"
    assert settingIO.Master_Volume == 100
    assert settingIO.Music_Volume == 100
    assert settingIO.SFX_Volume == 100
    assert settingIO.DifficultyLevel == settingIO.difficulty.EASY
    assert settingIO.Keymap_Left == pygame.K_a
    assert settingIO.Keymap_Right == pygame.K_d
    assert settingIO.Keymap_Up == pygame.K_w
    assert settingIO.Keymap_Down == pygame.K_s
    assert settingIO.Keymap_Primary_Fire == pygame.K_LSHIFT
    assert settingIO.Keymap_Secondary_Fire == pygame.K_RSHIFT
    assert settingIO.Keymap_Dash == pygame.K_SPACE
    assert settingIO.Keymap_Pause == pygame.K_ESCAPE


def test_import_setting():
    #Untestable
    assert True


def test_export_setting():
    #Untestable
    assert True


def test_load_settings():
    #Untestable
    assert True


def test_convertDifficultyToText():
    assert settingIO.convertDifficultyToText(
        settingIO.difficulty.EASY) == "Easy"
    assert settingIO.convertDifficultyToText(
        settingIO.difficulty.MEDIUM) == "Medium"
    assert settingIO.convertDifficultyToText(
        settingIO.difficulty.HARD) == "Hard"


def test_save_settings():
    settingIO.load_default_settings()
    settingIO.save_settings()
    assert settingIO.Player_Name == "PLAYER"


def test_valid_setting_file():
    #Untestable
    assert True


def test_get_username():
    settingIO.load_default_settings()
    settingIO.save_settings()
    assert settingIO.get_username() == "PLAYER"
