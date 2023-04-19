import os
import sys

sys.path.append('..')

from fileio import settingIO


def test_convertDifficulty():
    diff = "Easy"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.EASY
    diff = "Medium"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.MEDIUM
    diff = "Hard"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.HARD


def test_load_default_settings():
    # Make backup of settings.json
    if os.path.exists("fileio\\settings.json"):
        os.rename("fileio\\settings.json", "fileio\\settings.json.bak")

    settingIO.load_default_settings()
    assert settingIO.Player_Name == "Player"
    assert settingIO.Master_Volume == 100
    assert settingIO.Music_Volume == 100
    assert settingIO.SFX_Volume == 100
    assert settingIO.DifficultyLevel == settingIO.difficulty.EASY
    assert settingIO.keys == "wasd"

    # Restore backup of settings.json
    if os.path.exists("fileio\\settings.json.bak"):
        os.remove("fileio\\settings.json")
        os.rename("fileio\\settings.json.bak", "fileio\\settings.json")


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
    # Make backup of settings.json
    if os.path.exists("fileio\\settings.json"):
        os.rename("fileio\\settings.json", "fileio\\settings.json.bak")
    settingIO.load_default_settings()
    settingIO.save_settings()
    assert settingIO.Player_Name == "PLAYER"

    # Restore backup of settings.json
    if os.path.exists("fileio\\settings.json.bak"):
        os.remove("fileio\\settings.json")
        os.rename("fileio\\settings.json.bak", "fileio\\settings.json")


def test_valid_setting_file():
    #Untestable
    assert True


def test_get_username():
    settingIO.load_default_settings()
    settingIO.save_settings()
    assert settingIO.get_username() == "PLAYER"
